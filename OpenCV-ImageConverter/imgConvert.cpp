#include <opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/highgui/highgui_c.h>

using namespace cv;

int main( int argc, char** argv )
{
  
    // Creating a MAT object for the input image
    Mat image;
    // Load the image file
    image = imread("/Users/radugoada/Desktop/ImageConverter/Original_image.jpg", WINDOW_AUTOSIZE);
    
    if(!image.data) //Verifying if the image is available
    {
        printf( " No image data found!\n " );
        return -1;
    }
    
    // create a MAT object for gray image
    Mat gray_image;
    
    // Converting to Greyscale format
    // cvtColor( image, gray_image, CV_BGR2GRAY );
    cvtColor( image, gray_image, COLOR_BGR2GRAY );
    
    // Saving the transformed image to an output file
    imwrite( "GrayImage.jpg", gray_image );
    
    //Creating two separate windows
    namedWindow( "Original RGB Image", CV_WINDOW_AUTOSIZE );
    namedWindow( "Grayscaled Image", CV_WINDOW_AUTOSIZE );
    
    // imshow() - Displays an image in the specified window.
    // If the window was created with the CV_WINDOW_AUTOSIZE flag, the image is shown with its original size
    imshow( "Original", image );
    imshow( "Grayscale", gray_image );
    
    // Waiting for key press
    waitKey(0);
    destroyAllWindows();
    //Exit status, program finish
    return 0; 

}
