from PIL import Image


myImage = Image.open("mariana.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []

#pixel manipulation
for pixel in pixelList:
    red = pixel[0]
    green = pixel[1]
    blue = pixel[2]
    darkBlue = (0, 51,76)
    red2 = (217,26,33)
    lightBlue = (112,150,158)
    yellow = (252,227,166)

#find pixel indentation
    intensity = red + green + blue

    if (intensity <182):
        newPixelList.append(darkBlue)
    elif (intensity < 364) and (intensity > 182):
        newPixelList.append(red2)
    elif (intensity < 546) and (intensity > 364):
        newPixelList.append(lightBlue)
    else:
        newPixelList.append(yellow)
        


#open in the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()

