from PIL import Image


myImage = Image.open("ele2.jpg")
imageData = myImage.getdata()
pixelList = list(imageData)

newPixelList = []


#pixel manipulation
for pixel in pixelList:
	red = pixel[0]
	green = pixel[1]
	blue = pixel[2]

	average = ((red+blue+green)//3)
	
	newRed = 255 - pixel[0] #average #red*2
	if newRed > 255:
                newRed = 255

	newGreen = 255 - pixel[1]#average #green*2
	if newGreen > 255:
                newGreen = 255

	newBlue = 255 - pixel[2] #average #blue*3
	if newBlue > 255:
                newBlue = 255

	p = (newRed, newGreen, newBlue)

	#add pixel to new pixel list
	newPixelList.append(p)




#open in the image
newImage = Image.new("RGB", myImage.size)
newImage.putdata(newPixelList)
newImage.show()
