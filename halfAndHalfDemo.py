from PIL import Image

## Functions

def middle(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = ((red+blue+green)//3)
    
    newRed = average 
    if newRed > 255:
        newRed = 255

    newGreen = average 
    if newGreen > 255:
        newGreen = 255

    newBlue = average 
    if newBlue > 255:
        newBlue = 255

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)
    
def overExpose(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = ((red+blue+green)//3)
    
    newRed = red*2
    if newRed > 255:
        newRed = 255

    newGreen = green
    if newGreen > 255:
        newGreen = 255

    newBlue = blue
    if newBlue > 255:
        newBlue = 255

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)

def overBlue(pixel):
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]

    average = ((red+blue+green)//3)
    
    newRed = red
    if newRed > 255:
        newRed = 255

    newGreen = green
    if newGreen > 255:
        newGreen = 255

    newBlue = blue*2
    if newBlue > 255:
        newBlue = 255

    p = (newRed, newGreen, newBlue)
    newPixelList.append(p)



myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

length = len(pixelList)
part1 = length//3
part2 = part1*2

counter = 0


for pixel in pixelList:

    #pixel manipulation
    if(counter < part1):
        overExpose(pixel)
    elif counter < part2: 
        middle(pixel)
    else:
        overBlue(pixel)
    counter = counter + 1





#open in the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()
