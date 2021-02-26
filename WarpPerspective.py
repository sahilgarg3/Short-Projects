import cv2 as cv
import numpy as np


#########################################################################################
#                               Initialization
#########################################################################################
path = 'Resources/colorpic.jpg'
imgWidth, imgHeight = 720, 500
warp_width, warp_height = 250, 300
pointList = []
#########################################################################################
#########################################################################################
image = cv.imread(path)
image = cv.resize(image, (imgWidth, imgHeight))
image_copy = image.copy()
#########################################################################################


def get_warp(points, width, height):
    pos1 = np.float32(points)
    pos2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
    matrix = cv.getPerspectiveTransform(pos1, pos2)
    output = cv.warpPerspective(image_copy, matrix, (width, height))
    cv.imshow('Output', output)


def mouse_click(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONUP:
        pointList.append([x, y])
        cv.circle(image, (x, y), 5, (0, 0, 0), -1)
        cv.imshow('Image', image)


while True:
    if len(pointList) % 4 == 0 and len(pointList) != 0:
        get_warp(pointList[-4:], warp_width, warp_height)
    cv.imshow('Image', image)
    cv.setMouseCallback('Image', mouse_click)

    if cv.waitKey(1) & 0xFF == ord('r'):
        pointList = []
        image = cv.imread(path)
        image = cv.resize(image, (imgWidth, imgHeight))
        cv.destroyWindow('Output')
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
