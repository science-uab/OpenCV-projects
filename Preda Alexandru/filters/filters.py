import cv2
import sys
from time import sleep
import numpy as np

cascPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascPath)

video_capture = cv2.VideoCapture(0)
frame = video_capture.read()[1]

mustata = cv2.imread('images/2.jpg')
palarie = cv2.imread('images/cowboy_hat.png')



def pune_mustata(mustata, fc, x, y, w, h):
    face_width = w
    face_height = h

    mustata_width = int(face_width * 0.416) + 1
    mustata_height = int(face_height * 0.142) + 1

    mustata = cv2.resize(mustata, (mustata_width, mustata_height))

    for i in range(int(0.628 * face_height), int(0.628 * face_height) + mustata_height):
        for j in range(int(0.291 * face_width), int(0.291 * face_width) + mustata_width):
            for k in range(3):
                if mustata[i - int(0.628 * face_height)][j - int(0.291 * face_width)][k] < 235:
                    fc[y + i][x + j][k] = \
                        mustata[i - int(0.628 * face_height)][j - int(0.291* face_width)][k]
    return fc


def pune_palarie(palarie, fc, x, y, w, h):
    face_width = w
    face_height = h

    palarie_width = face_width + 1
    palarie_height = int(0.35 * face_height) + 1

    palarie = cv2.resize(palarie, (palarie_width, palarie_height))

    for i in range(palarie_height):
        for j in range(palarie_width):
            for k in range(3):
                if palarie[i][j][k] < 235:
                    fc[y + i - int(0.25 * face_height)][x + j][k] = palarie[i][j][k]
    return fc



ch = 0
print( "Selecteaza un filtru: " "1.) Palarie ""2.) Mustata ""3.) Palarie si mustata")
ch = int(input())

while True:
    if not video_capture.isOpened():
        print('Nu am putut deschide camera!')
        sleep(5)
        pass

    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(70, 70)
    )

    for (x, y, w, h) in faces:
        if ch == 2:
            frame = pune_mustata(mustata, frame, x, y, w, h)
        elif ch == 1:
            frame = pune_palarie(palarie, frame, x, y, w, h)
        elif ch == 3:
            frame = pune_mustata(mustata, frame, x, y, w, h)
            frame = pune_palarie(palarie, frame, x, y, w, h)


    cv2.imshow('Aplicatie Video', frame)

    k = cv2.waitKey(1)
    if k == ord('c'):
        break
    elif k == ord('s'):
        cv2.imwrite(filename='images/test.png', img=frame)

video_capture.release()
cv2.destroyAllWindows()