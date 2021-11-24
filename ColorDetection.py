import cv2 as cv
import pandas as pd

image = cv.imread('Resources/colorpic.jpg')
image = cv.resize(image, (800, 600))
df = pd.read_csv('Resources/colors.csv', header=None, names=['Colors', 'Colors_Name', 'Hash Value', 'R', 'B', 'G'])

clicked = False
r = b = g = 0


def color_detection(R, G, B):
    minimum = 1000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'Colors_Name']
    return cname


def click_event(event, x, y, flags, params):
    if event == cv.EVENT_LBUTTONUP:
        global b, g, r, clicked
        clicked = True
        b, g, r = image[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


cv.namedWindow('Image')
cv.setMouseCallback('Image', click_event)

while True:
    cv.imshow('Image', image)
    if clicked:
        cv.rectangle(image, (20, 20), (600, 60), (b, g, r), -1)
        text = color_detection(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
        cv.putText(image, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv.LINE_AA)
        if r + g + b >= 600:
            cv.putText(image, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv.LINE_AA)
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
