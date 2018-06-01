# @author Malai Mihai
import cv2

# load image
image = cv2.imread("example.jpg")
# convert from rgb to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# apply blur to reduce noice, this will be useful when applying canny algorithm
gray = cv2.GaussianBlur(gray, (3, 3), 0)
# display grayed image
cv2.imshow("Gray", gray)
# wait for 'x' btn
cv2.waitKey(0)

# detect edges of image
edged = cv2.Canny(gray, 10, 250)
# display edged image
cv2.imshow("Edged", edged)
# wait for 'x' btn
cv2.waitKey(0)

# construct and apply a closing structuring element
structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, structuringElement)
# display edged image
cv2.imshow("Closed", closed)
# wait for 'x' btn
cv2.waitKey(0)

#find contours
_, cnts, _ = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

total = 0
for c in cnts:
    # approximate the contour
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.03 * peri, True)

    # if approximated contour has 4 points, draw blue contours over object and assume that this is an rectangle
    if len(approx) == 4:
        cv2.drawContours(image, [approx], -1, (255, 0, 0), 5)
        total += 1

print "Nr of rectangles: {0}".format(total)
cv2.imshow("Output", image)
cv2.waitKey(0)
