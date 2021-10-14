#----- Important things to note -----
# PYTHON VERSION HAS TO BE 3.7+
# background images HAVE to be 640 by 480 to work

import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640) #640 is for width
cap.set(4, 480) #480 is for height
# cap.set(cv2.CAP_PROP_FPS, 60)

segmentor = SelfiSegmentation() #defualt model number is 1 -> ladscape mode
fpsReader = cvzone.FPS() #gets the FPS of the current frames displayed

# imgBG = cv2.imread("BackgroundImages/3.jpg")

listImg = os.listdir("C:/Users/Tarun/Desktop/comp/pycharm/back_remove/Background_images/")
imgList = [] #list containing all background images
for imgPath in listImg:
    img = cv2.imread(f'C:/Users/Tarun/Desktop/comp/pycharm/back_remove/Background_images/{imgPath}')
    imgList.append(img)
print(imgList)
indexImg = 0

while True:
    success, img = cap.read()
    # imgOut = segmentor.removeBG(img, (255,0,255), threshold=0.83) # purple background for color ( no background image , only plain color ) , threshold value -> 1 cuts everything ( only background ) , recommended background is 0.8
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.8)
    imgStack = cvzone.stackImages([img, imgOut], 2,1) #stacks the 2 different frames - > 1 for original , 1 for image with new background
    _, imgStack = fpsReader.update(imgStack) #adds the fps number on the final output image
    #_, imgStack = fpsReader.update(imgStack,color=(0,0,255)) # can change color if desired
    print("Number of image used : ",indexImg+1)
    cv2.imshow("image", imgStack)
    key = cv2.waitKey(1)
    if key == ord('a'): #if click on 'a' go back 1 photo
        if indexImg>0:
            indexImg -=1
    elif key == ord('d'): #if click on 'd' go forward 1 photo
        if indexImg<len(imgList)-1:
            indexImg +=1
    elif key == ord('q'): #if 'q' break out of loop
        break