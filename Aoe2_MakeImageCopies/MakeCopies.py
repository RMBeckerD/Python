from PIL import Image
import os

nImages = input("Number of Copies: ")
n = int(nImages)
inputPath = input("Input Image Name: ")
suffix = input("NumberSuffix: ")
inputImage = Image.open(inputPath + ".bmp")

numberStr = ""
for i in range(n):
	numberStr = str(i + 1)
	while len(numberStr) < len(nImages) + 1:
		numberStr = "0" + numberStr
	inputImage.save(inputPath + "_" + numberStr + suffix + ".bmp")
	