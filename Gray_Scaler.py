import glob
import os
from PIL import Image


dir_path = "/home/Halivious/Desktop/All_Data/All_images/" +"*.jpg"
filenames = glob.glob(dir_path)
k=0

for filename in filenames:
  if k == 182797 :
    break
  with Image.open(filename) as im:
     
     k +=1
     output_dir= "/home/htranaliz/Desktop/All_Data/All_images_Gray/"+str(k) +"*.jpg"
     im = im.convert('L')
     im.save(os.path.join(filename, output_dir))
     print(output_dir)
      
  
    
    
