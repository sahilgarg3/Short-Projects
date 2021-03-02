import cv2 as cv
import os

path = 'Images'

for folder in os.listdir(path):
    files = os.listdir(path + '/' + folder)
    images = []
    for file in files:
        image = cv.imread(path + '/' + folder + '/' + file)
        image = cv.resize(image, (0, 0), None, 0.2, 0.2)
        images.append(image)

    stitcher = cv.Stitcher.create()
    (status, result) = stitcher.stitch(images)
    if status == cv.STITCHER_OK:
        print("Panorama generated successful")
        cv.imshow(folder, result)
        cv.waitKey(1)
    else:
        print('Panorama Generation Unsuccessful')
cv.waitKey(0)
