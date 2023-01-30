import glob
import os
from PIL import Image

k=0



def find_char(string, char):
  for i in range(len(string)):
    if string[i] == char:
      return i
  return -1

char = "/"
empty = ""

# Set the directory path
dir_path = '/home/Halivious/Desktop/All_Data/All_images_Gray/*.jpg'


# Use glob to find all the files that match the pattern
filenames = glob.glob(dir_path)

# Iterate over the filenames
for filename in filenames:
  if k == 182797 :
    break
       	
   
  # Open the image file
  with Image.open(filename) as im:
    
    text = "/home/Halivious/Desktop/0013/*.jpg"
    k +=1
    splitter = text.split('*')
    text_out = splitter[-1]
    output_dir= '/home/Halivious/Desktop/All_Data/Total_Output_Gray_Resized/' + str(k)+str(text_out)
    print(k)
    

    
    #print("oo:", filename)
    # Resize the image
    im_resized =im.resize((32,32))
    
    
    
    
    # Save the resized image
    im_resized.save(os.path.join(filename, output_dir))

