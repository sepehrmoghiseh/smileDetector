'''
a very simple smile-detector for images with use of cv2 and haarcascade
@author: Sepehr-Moghiseh
@date:03/11/2021
@version:01
'''
import cv2
import shutil

dir = input("enter the path of the Image! : \n  ")

image = cv2.imread(dir)

smile_cascade = cv2.CascadeClassifier(r'haarcascade\haarcascade_smile.xml')

smiles = smile_cascade.detectMultiScale(image, scaleFactor=2, minNeighbors=10)

for (sx, sy, sw, sh) in smiles:
    cv2.rectangle(image, (sx, sy), ((sx + sw), (sy + sh)), (4, 120, 112), 4)

cv2.imshow("Smile Detected", image)
cv2.waitKey(0)
cv2.imwrite("savedImage.jpg",image)
cv2.destroyAllWindows()
