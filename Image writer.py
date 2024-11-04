# imageWriter.py

img = open("testimage.ppm","w")

img.write("P6") #magic number
img.write("640 480") #width and height
img.write("255") #Max colour depth

# Fill all pixels in red 
' ' '
for pixel in range(640):
    for pixer in range(640): 
        img.write("255 0 0 ")
   

img.close()
    
# Challenges:
# 1. fill all pixels with blue
# 2. fil all pixels with greem
