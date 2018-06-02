//Melentii Evghenii

#include "stdafx.h"
#include <stdio.h>
#include <math.h>
#include <opencv\cv.h>
#include <opencv\highgui.h>
#include <opencv2\objdetect\objdetect.hpp>
#include <opencv2\highgui\highgui.hpp>
#include <opencv2\imgproc\imgproc.hpp>
#include <vector>

using namespace cv;
using namespace std;

int main()
{
	CascadeClassifier face_cascade, eye_cascade;
	if (!face_cascade.load("C:\\opencv\\build\\etc\\haarcascades\\haarcascade_frontalface_default.xml")) {
		printf("cannot find cascade face");
		return 1;
	}
	if (!eye_cascade.load("C:\\opencv\\build\\etc\\haarcascades\\haarcascade_eye.xml")) {
		printf("cannot find cascade eye");
		return 1;
	}
	VideoCapture capture(0); 
	if (!capture.isOpened())
	{
		printf("cannot detect camera");
		return 1;
	}
	Mat cap_img, gray_img;
	vector<Rect> faces, eyes;
	Point pt1, pt2;
	while (1)
	{
		capture >> cap_img;
		cvtColor(cap_img, gray_img, CV_BGR2GRAY);
		face_cascade.detectMultiScale(gray_img, faces, 1.3, 5);
		for (int i = 0; i < faces.size(); i++)
		{
			pt1.x = faces[i].x + faces[i].width;
			pt1.y = faces[i].y + faces[i].height;

			pt2.x = faces[i].x;
			pt2.y = faces[i].y;
			rectangle(cap_img, pt1, pt2, cvScalar(0, 255, 0), 2);
			Mat faceROI = gray_img(faces[i]);
			eye_cascade.detectMultiScale(faceROI, eyes);
			for (size_t j = 0; j< eyes.size(); j++)
			{
				pt2.x = faces[i].x + eyes[j].x;
				pt2.y = faces[i].y + eyes[j].y;
				pt1.x = pt2.x + eyes[j].width;
				pt1.y = pt2.y + eyes[j].height;
				rectangle(cap_img, pt1, pt2, cvScalar(0, 0, 255), 2);
			}
		}
		imshow("Detection", cap_img);
		if (waitKey(1) == 27)
			break;
	}
	return 0;
}