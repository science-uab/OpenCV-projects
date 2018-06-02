# Finger detection

This project will count fingers in a given video frame using c++ and openCV.

### How it works
1. Convert the video frame from BGR to Gray
2. Perform a Threshold OTSU
3. Perform a GBlur
4. Find the Biggest Contour(this will be the hand)
5. Perform a convexHull and mark the Region of interst
6. Count the Items
7. Display it
### Example
![Alt text](FingerDetection.png?raw=true "Title")
### License
MIT
### Author
Iancu Mihai-Ovidiu
