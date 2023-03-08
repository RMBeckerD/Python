from PIL import Image
import os

inputPath = input("Input Image name: ")
outputPath = input("Output Image suffix: ")
inputImage = Image.open(inputPath + ".png")

inWidth, inHeight = inputImage.size
outputImage = Image.new('RGBA',(inWidth, inHeight))

for x in range(inWidth):
	for y in range(inHeight):

		r, g, b, a = inputImage.getpixel((x,y))
		outputImage.putpixel((x,y),(0, g, 0, 255))

outputImage.save(inputPath + outputPath + ".png")