import cv2 as cv
import numpy as np


def concat(scale, ImageList):
    rows = len(ImageList)
    if type(ImageList[0]) == list:

        lengths = [len(i) for i in ImageList]
        cols = max(lengths)
        blank = np.zeros((ImageList[0][0].shape[0], ImageList[0][0].shape[1]), np.uint8)
        for i in range(rows):
            while len(ImageList[i]) != cols:
                ImageList[i].append(blank)

        for x in range(0, rows):
            for y in range(0, cols):
                if len(ImageList[x][y].shape) == 2:
                    ImageList[x][y] = cv.cvtColor(ImageList[x][y], cv.COLOR_GRAY2BGR)
                if ImageList[0][0].shape[:2] == ImageList[x][y].shape[:2]:
                    ImageList[x][y] = cv.resize(ImageList[x][y], (0, 0), None, scale, scale)
                else:
                    ImageList[x][y] = cv.resize(ImageList[x][y], (ImageList[0][0].shape[1], ImageList[0][0].shape[0]),
                                                None, scale, scale)

        blankImage = np.zeros((ImageList[0][0].shape[0], ImageList[0][0].shape[1]), np.uint8)
        hor = [blankImage] * rows
        for x in range(0, rows):
            hor[x] = np.hstack(ImageList[x])
        ver = np.vstack(hor)

    else:
        for x in range(0, rows):
            if ImageList[0].shape[:2] == ImageList[x].shape[:2]:
                ImageList[x] = cv.resize(ImageList[x], (0, 0), None, scale, scale)
            else:
                ImageList[x] = cv.resize(ImageList[x], (ImageList[0].shape[1], ImageList[0].shape[0]),
                                         None, scale, scale)

            if len(ImageList[x].shape) == 2:
                ImageList[x] = cv.cvtColor(ImageList[x], cv.COLOR_GRAY2BGR)
        hor = np.hstack(ImageList)
        ver = hor

    return ver


image = cv.imread('Resources/images 0.jpg')
image = cv.resize(image, (600, 500))
Gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
Blur = cv.GaussianBlur(Gray, (7, 7), 1)
Canny = cv.Canny(Blur, 100, 130)
kernel = np.ones((5, 5), np.uint8)
Dilation = cv.dilate(Canny, kernel, iterations=1)
Erode = cv.erode(Dilation, kernel, iterations=1)

imgResult = concat(0.4, [[image, Gray, Blur], [Canny, Dilation, Erode]])
# imgResult = concat(0.4, [[image, Gray, Blur], [Canny]])       # Insert Black Images
cv.imshow('Result', imgResult)
cv.waitKey(0)
