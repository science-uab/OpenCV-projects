//Author Iancu Mihai-Ovidiu

#include "opencv2/imgproc/imgproc.hpp"
#include <opencv2/highgui/highgui.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main(int argc, const char** argv)
{
	Mat image;
	Mat image_threshold;
	Mat image_gray;
	Mat image_region;
	char destination[40];
	int count = 0;
	vector<vector<Point>> contours;
	vector<Vec4i> hierarchy;
	Point2f rect_point[4];

	VideoCapture cam(0);
	if (!cam.isOpened()) {
		cout << "" << endl;
		return -1;
	}

	namedWindow("Original image", CV_WINDOW_AUTOSIZE);
	namedWindow("Gray image", CV_WINDOW_AUTOSIZE);
	namedWindow("Thresholded image", CV_WINDOW_AUTOSIZE);
	namedWindow("Region of interes", CV_WINDOW_AUTOSIZE);

	while (1) {
		bool b = cam.read(image);
		if (!b) {
			cout << "ERROR : cannot read" << endl;
			return -1;
		}
		Rect region_of_interes(340, 100, 270, 270);
		image_region = image(region_of_interes);
		cvtColor(image_region, image_gray, CV_RGB2GRAY);

		GaussianBlur(image_gray, image_gray, Size(19, 19), 0.0, 0);
		threshold(image_gray, image_threshold, 0, 255, THRESH_BINARY_INV + THRESH_OTSU);
		findContours(image_threshold, contours, hierarchy, CV_RETR_EXTERNAL, CV_CHAIN_APPROX_SIMPLE, Point());

		if (contours.size()>0) {
			size_t index = -1;
			size_t size = 0;

			for (size_t i = 0; i < contours.size(); i++) {
				if (contours[i].size() > size) {
					size = contours[i].size();
					index = i;
				}
			}
			vector<vector<int>> hull(contours.size());
			vector<vector<Point>> hullPoint(contours.size());
			vector<vector<Vec4i>> defects(contours.size());
			vector<vector<Point>> defectPoint(contours.size());
			vector<vector<Point>> contours_poly(contours.size());
			vector<RotatedRect> minRect(contours.size());
			vector<Rect> boundRect(contours.size());

			for (size_t i = 0; i<contours.size(); i++) {
				if (contourArea(contours[i])>5000) {
					convexHull(contours[i], hull[i], true);
					convexityDefects(contours[i], hull[i], defects[i]);
					if (index == i) {
						minRect[i] = minAreaRect(contours[i]);
						for (size_t k = 0; k<hull[i].size(); k++) {
							int ind = hull[i][k];
							hullPoint[i].push_back(contours[i][ind]);
						}
						count = 0;

						for (size_t k = 0; k<defects[i].size(); k++) {
							if (defects[i][k][3]>13 * 256) {
								int p_start = defects[i][k][0];   
								int p_end = defects[i][k][1];
								int p_far = defects[i][k][2];
								defectPoint[i].push_back(contours[i][p_far]);
								circle(image_region, contours[i][p_end], 3, Scalar(0, 255, 0), 2);
								count++;
							}
						}

						if (count == 1)
							strcpy(destination, "One");
						else if (count == 2)
							strcpy(destination, "Two");
						else if (count == 3)
							strcpy(destination, "Three");
						else if (count == 4)
							strcpy(destination, "Four");
						else if (count == 5)
							strcpy(destination, "Five");
						else
							strcpy(destination, "No finger detected");

						putText(image, destination, Point(70, 70), CV_FONT_HERSHEY_SIMPLEX, 2, Scalar(255, 255, 255), 2, 8, false);
						approxPolyDP(contours[i], contours_poly[i], 3, false);
						boundRect[i] = boundingRect(contours_poly[i]);
						rectangle(image_region, boundRect[i].tl(), boundRect[i].br(), Scalar(0, 255, 0), 2, 8, 0);
						minRect[i].points(rect_point);
						for (size_t k = 0; k<4; k++) {
							line(image_region, rect_point[k], rect_point[(k + 1) % 4], Scalar(0, 0, 255), 2, 8);
						}
					}
				}
			}
			imshow("Original_image", image);
			imshow("Gray_image", image_gray);
			imshow("Thresholded_image", image_threshold);
			imshow("Region of interes", image_region);
			if (waitKey(1) == 27) {
				return -1;
			}
		}
	}

	return 0;
}