from PIL import Image
import glob
files = glob.glob("*.*")

  
# get image
filepath = r"C:\Users\jayst\Downloads\chords.png"
# C:\projects\python\resizedBeach1.png

filepath = r"C:\projects\node\flip\vflip\x.jpg"
img = Image.open(filepath)
  
# get width and height
width = img.width
height = img.height
  
# display width and height
print(f"The height of the image {filepath} is {height} ")
print(f"The width of the image is: {width} ", )
