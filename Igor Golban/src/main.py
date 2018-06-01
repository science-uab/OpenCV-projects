import numpy as np
import cv2


lion = cv2.imread('lion.jpg')
savana = cv2.imread('savana.jpg')


lion2hsv = cv2.cvtColor(lion, cv2.COLOR_BGR2HSV)

# hsv hue sat val
green_l = np.array([35, 38, 70])
green_u = np.array([150, 255, 255])

mask = cv2.inRange(lion2hsv, green_l, green_u)
mask_inv = cv2.bitwise_not(mask)

savana_bg = cv2.bitwise_and(savana, savana, mask=mask)
lion_bg = cv2.bitwise_and(lion, lion, mask=mask_inv)

final = cv2.add(lion_bg, savana_bg)

cv2.imshow('mask', mask)
cv2.imshow('lion', lion)
cv2.imshow('savana', savana)
cv2.imshow('lion_bg', lion_bg)
cv2.imshow('savana_bg', savana_bg)
cv2.imshow('final', final)

cv2.imwrite('result.jpg', final)


def getcoord(event,x,y,flags,param):
    global ix,iy
    if event == 1:
        print 'Click: x=',x,'y=',y
        print lion2hsv[y, x], lion_bg[y, x]

def demowhile():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',getcoord)
    while (1):
        cv2.imshow('image', lion_bg)
        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break
#demowhile()


cv2.waitKey(0)
cv2.destoyAllWindows()