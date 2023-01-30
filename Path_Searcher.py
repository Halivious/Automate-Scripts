import os 

for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        if file =="model.onnx" :
           print(os.path.join(root,file))
           
        else :
           print("haydaaa hocam ne diyor bu")   

