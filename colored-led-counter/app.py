# import the necessary packages
import argparse
import numpy as np
from pprint import pprint


try:
    from cv2 import cv2

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True,
                    help="path to the input image")
    ap.add_argument("-c", "--color",
                    default="red",
                    help="red, green, blue, yellow")
    args = vars(ap.parse_args())

    img_path = 'leds/' + args['image']
    img = cv2.imread(img_path) # type: numpy.ndarray

    #scale
    max_dimension = max(img.shape)
    scale = 816/max_dimension

    # reval, threshold = cv2.threshold(img, 85, 220, cv2.THRESH_BINARY)

    img = cv2.resize(img, None, fx=scale, fy=scale)

    color = args['color']

    if color == 'yellow':
        alpha = 2
        beta = 30
    else:
        alpha = 2
        beta = 30

    img =cv2.addWeighted(img, alpha, np.zeros(img.shape, img.dtype), 0, beta)

    img = cv2.GaussianBlur(img, (7,7), 0)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower_green = np.array([55, 100, 50])
    upper_green = np.array([85, 255, 255])

    lower_yellow = np.array([30, 20, 50])
    upper_yellow = np.array([60, 255, 255])

    lower_blue = np.array([90, 100, 50])
    upper_blue = np.array([150, 255, 255])

    lower_red = np.array([0, 50, 50])
    upper_red = np.array([20, 255, 255])

    lower_cold_red = np.array([160, 50, 50])
    upper_cold_red = np.array([255, 255, 255])

    if color == 'red':
        mask = cv2.inRange(hsv, lower_red, upper_red)
        mask2 = cv2.inRange(hsv, lower_cold_red, upper_cold_red)
        mask = cv2.bitwise_or(mask, mask2)

    if color == 'green':
        mask = cv2.inRange(hsv, lower_green, upper_green)

    if color == 'blue':
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

    if color == 'yellow':
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

    res = cv2.bitwise_and(img, img, mask=mask)


    cv2.imshow('img', img)
    cv2.imshow('res', res)

    new_res = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
    new_res = cv2.bitwise_and(new_res, new_res, mask=mask)
    new_res = cv2.cvtColor(new_res, cv2.COLOR_BGR2GRAY)
    reval, new_res = cv2.threshold(new_res, 10, 220, cv2.THRESH_BINARY)

    cv2.imshow('new_res', new_res)

    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (15,15))
    mask_closed = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask_clean = cv2.morphologyEx(mask_closed, cv2.MORPH_OPEN, kernel)

    image, contours, hierarchy = cv2.findContours(new_res.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]

    led_contours = list(filter(lambda x: x[0] > 20 and x[0] < 300 , contour_sizes))

    nr_leds = len(led_contours)


    print(str(nr_leds) +' LEDs' )
    print('Press escape')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

except ImportError:
    print("Ooops..")