# imageWriter.py

img = open("testimage.ppm","w")

img.write("P6") #magic number
img.write("640 480") #width and height
img.write("255") #Max colour depth

for pisxel in range(640):
    for pixer in range(640): 
        img.write("255 0 0 ")
   

q  img.close()
    
