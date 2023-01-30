import imgaug.augmenters as iaa
from imgaug import parameters as iap
from PIL import Image
import numpy as np
import glob
import random

Pathway="/home/Halivious/Videos/Frames/"
Extension = "*.jpg"
data=glob.glob(Pathway+Extension)
Array_Point = 0
Loop_Counter = 3

def sequence_1():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)
	Randomize_Number_Rotate_Positive=random.randint(0,45)
	Randomize_Number_Rotate_Negative=random.randint(-45,0)
	Randomize_Number_GaussianNoise =random.randint(0,32)

	seq = iaa.Sequential([
	    iaa.Affine(rotate=iap.Uniform(Randomize_Number_Rotate_Positive, Randomize_Number_Rotate_Negative)),
	    iaa.AdditiveGaussianNoise(scale=Randomize_Number_GaussianNoise)
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")	
	
	
def sequence_2():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)
	Randomize_Number_Brightness =random.randint(1,5)

	seq = iaa.Sequential([
	    iaa.Resize((0.5, 1.0)),
	    iaa.imgcorruptlike.Brightness(Randomize_Number_Brightness)
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")	
	
	
def sequence_3():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)
	Randomize_Number_Flipper =random.randint(0,10)
	

	seq = iaa.Sequential([
	   iaa.Fliplr(Randomize_Number_Flipper/10),
	   iaa.GammaContrast((0.5, 2.0))
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")
	
def sequence_4():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)

	seq = iaa.Sequential([
	   iaa.ChangeColorTemperature((1100, 10000)),
	   iaa.AddToHue((-50, 50))
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")	
		
		
def sequence_5():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)
	Randomize_Number_Glassblur =random.randint(1,4)
	Randomize_Number_Saturation =random.randint(1,4)

	seq = iaa.Sequential([
	   iaa.MedianBlur(k=(3,11)),
	   iaa.imgcorruptlike.Saturate(severity=Randomize_Number_Saturation)
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")		
	
def sequence_6():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)
	Randomize_Number_iterations =random.randint(1,3)
	

	seq = iaa.Sequential([
	   iaa.MotionBlur(k=15),
	   iaa.Cutout(nb_iterations=Randomize_Number_iterations)
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")			
	
	
def sequence_7():
       
	image = Image.open(data[Array_Point])
	image = np.asarray(image)
	Randomize_Number_SaltAndPepper =random.randint(1,6)
	
	seq = iaa.Sequential([
	   iaa.SaltAndPepper(Randomize_Number_SaltAndPepper/10, per_channel=True)
	])
	augmented_image = seq(image=image)
	augmented_image = Image.fromarray(augmented_image)
	augmented_image.save("/home/Halivious/augmented/Augmented_Frame"+str(Array_Point)+"_"+str(Loop_Counter)+".jpg")		
	
						

while(True):

   Decider = random.randint(1,7)
   if(Array_Point==1977):
      Array_Point== 0
      Loop_Counter +=1
      
   if(Loop_Counter==4):
      break   
   if(Decider==1):
      sequence_1()
      print("Seq 1 active")
      
   elif(Decider==2):
       sequence_2()  
       print("Seq 2 active")
       
   elif(Decider==3):
       sequence_3()
       print("Seq 3 active")  
       
   elif(Decider==4):
       sequence_4()
       print("Seq 4 active") 
        
   elif(Decider==5):
       sequence_5()
       print("Seq 5 active")  
            
   elif(Decider==6):
       sequence_6()
       print("Seq 6 active")  
      
   elif(Decider==7):
       sequence_7()
       print("Seq 7 active")  
      
   Array_Point +=1
   print(Array_Point)   

   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   


