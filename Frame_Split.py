import cv2
from pathlib import Path
import glob

image_dir= Path("/home/Halivious/Videos/Frames/")
count = len(list(image_dir.glob('*.jpg')))
print(count)
cap1 = cv2.VideoCapture("/home/Halivious/Videos/1.mkv")
cap2 = cv2.VideoCapture("/home/Halivious/Videos/2.mkv")
cap3 = cv2.VideoCapture("/home/Halivious/Videos/3.mkv")

i=0

while(cap1.isOpened()):
    ret, frame = cap1.read()
    if ret == False:
        break
    cv2.imwrite("/home/Halivious/Videos/Frames/frame"+str(i)+".jpg",frame)
    i +=1
    
cap1.release() 
while(cap2.isOpened()):
    ret, frame = cap2.read()
    if ret == False:
        break
    cv2.imwrite("/home/Halivious/Videos/Frames/frame"+str(i)+".jpg",frame)
    i +=1
    
cap2.release()    
    
while(cap3.isOpened()):
    ret, frame = cap3.read()
    if ret == False:
        break
    cv2.imwrite("/home/Halivious/Videos/Frames/frame"+str(i)+".jpg",frame)
    i +=1
    
cap3.release()    
    
      
    
    

cv2.destroyAllWindows()        
