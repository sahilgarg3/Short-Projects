# Short-Projects

## [Concatenation](Concatenation.py)
`Concat` function is to merge or stack the n number of images into rows and columns depending upon the user's input. 

The inputs of `concat` function are as follows:
- Scale Value
- List of Images

The scale value resize the original image. 

Whereas, list of Images is the list of the images to be concatinated. 

To put the images in one row, define all the images in that list. But if you want to concat images into multiple rows and columns then put the images in nested list and pass it to the function. 
```
concat(0.4, [[image, Gray, Blur], 
             [Canny, Dilation, Erode]])
```

> Nested list is in 2 x 3 matrix, that's why the images are concat in the matrix of 2 x 3.

![Concatination 1](https://user-images.githubusercontent.com/79501547/140706782-15c97952-96a4-4986-b0c0-a4930ab2a683.png)

If, the length of each list element in the final list is not same, then a black image will take place of the next element in the list/s having less number of elements and display the black image with other images of the row.

```
concat(0.4, [[image, Gray, Blur], 
             [Canny]])
```
> In this nested list, one list has the length of 3 and other has 1, So the rows would be the same which is the length of the input list but the column would be equal to the length of the list with maximum elements. Blank Images would be appended to the list with less number of elements.

![Concatination 2](https://user-images.githubusercontent.com/79501547/140711339-2cd4929c-1d90-4714-8f5a-252651dbb746.png)


## [Warp Perspective](WarpPerspective.py)

### User Initialization
- Path of the Image
- Width & Height of the Image
- Width & Height of the Warped Image.

Sometimes the images or videos captured may not be aligned for us to view enough information from the images or videos, in such cases, it is necessary to align such images or videos to obtain better insights from the images or videos and in order to be able to change the perspective of the images or videos to obtain more useful information from the images or videos, we make use of a function called `getPerspectiveTransform()` function and the changed perspective of the images or videos must be fit to the original images or videos and this can be done using a function called `warpPerspective()` function in OpenCV.

OpenCV provides a facility to use the mouse as a paint brush or a drawing tool. Whenever any mouse event occurs on the window screen, it can draw anything. Mouse events can be left-button down, left-button up, double-click, etc. It gives us the coordinates (x,y) for every mouse event. By using these coordinates, we can draw whatever we want using `setMouseCallback()`

> At First, you'll see this image

![plot](https://github.com/sahilgarg3/Short-Projects/blob/main/Resources/colorpic.jpg)

> After two clicks

![Warp Per 1](https://user-images.githubusercontent.com/79501547/140720189-3058d03e-34e3-411e-8184-6ef02a940ffe.png)

> After three clicks

![Warp Per 2](https://user-images.githubusercontent.com/79501547/140720328-b4526af7-3312-4d90-8cc9-08588c938577.png)

> After four clicks and the warped image alongside with the window named as Output.

![Warp Per 3](https://user-images.githubusercontent.com/79501547/140720583-ca1adff0-162a-48aa-962c-2cc1fe8d4f2c.png)

> One can continue marking the points even after getting the previous output to get the warped image of new selected points
> Click `r` to **reset** the list and `q` to **exit** the program

## [Color Detection](ColorDetection.py)
> Click at any place on the image to get the most similar defined color name.

![Color D1](https://user-images.githubusercontent.com/79501547/140721990-069c343f-f17c-4d84-bfa5-8ec7c85a7fc7.png)
![Color D2](https://user-images.githubusercontent.com/79501547/140722014-e0a76bfb-df99-4adb-8ffd-234dd2b5fe92.png)


## [Panorama](panorama.py)
Stiching n number of images into one to create a single image with similar characteristics.


---
> Keep smiling and work harder
---
