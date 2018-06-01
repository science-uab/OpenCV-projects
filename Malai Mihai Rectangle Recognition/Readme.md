# Rectangle recognition

This script will count rectangle in a given image using python and openCV.

To run the application type: ```python detect_rectangle.py```

### How it works
1. Loads the image from disk and convert it to grayscale.
2. Blur the image to get a better detection of edges
3. Apply the Canny edge detector to detect edges
4. Apply a morphological  operation to close any gaps in the outlines.
5. Find the contours.
6. Apply contour approximation and count values, if value is 4 we may assume that the object is an rectangle
### Example
![Alt text](example.jpg?raw=true "Title")
![Alt text](example_final.jpg?raw=true "Title")
### License
MIT
### Author
Malai Mihai

