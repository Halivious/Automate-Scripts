import pyautogui
import cv2
import numpy as np
import time


resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "Recording2.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
start = time.time()
while(True):
        
	img = pyautogui.screenshot()
	end = time.time()
	if (end-start == 5):
	      break
	print(end - start)
	frame = np.array(img)
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	out.write(frame)
	cv2.imshow('Live', frame)
	if (end-start == 5):
	      break
	    
	    
	    
Capturer=cv2.VideoCapture('/home/Halivious/Desktop/Recording2.avi')
frameNr = 0
 
while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'/home/Halivious/Desktop/output/frame_{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()	    
out.release()    
cv2.destroyAllWindows()
