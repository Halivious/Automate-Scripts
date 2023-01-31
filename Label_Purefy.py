import glob
from PIL import Image 
import PIL

Path_Text="/home/Halivious/Labeled/"
Extension_Text = "*.txt"

Path_Images ="/home/Halivious/Videos/augmented/"
Extension_Image = "*.jpg"
Extension_Image2 = ".jpg"

Text = Path_Text+Extension_Text
Data_Point = 0

data = []
data = glob.glob(Text)
while(True):
    
    splitter = data[Data_Point].split("/")
    Text_File = splitter[-1]
    Image_Array = Text_File.split(".")
    Image_Temper =Image_Array[0] 
    print(Image_Temper)

    Full_Images = Image_Temper+Extension_Image2
    my_image = Image.open(Path_Images+Full_Images)
    image = my_image.save("/home/Halivious/Pure_Images/"+Full_Images)
    print("Done",image)
    Data_Point +=1
