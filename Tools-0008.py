
from PIL import Image,ImageDraw

def addText(img,string):
    size = img.size
    width = size[0] - 20
    high = size[1] - 20
    lenth = len(string)*3
    draw = ImageDraw.Draw(img)
    draw.text((width-lenth,high),string,fill='black')
    oriImg.show()
    oriImg.save(path)

path = input("Please input the image file with path: ")
try:
    print("path: "+path)
    oriImg = Image.open(path)
    addText(oriImg,"good")
except IOError:
    print("can't' open the file,check the path again")
    newImg = Image.new('RGBA',(320,240),'white')
    newImg.save(path)

    
