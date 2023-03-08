from PIL import Image
import os

iterations = int(input("Number of iterations: "))
it = 0
while it < iterations:
	print("Iteration: (" + str((it + 1)) + "/" + str(iterations) + ")")
	# Images path gather
	inputPath = ""
	answer1 = 0
	while answer1 < 1 or answer1 > 6:
		print("A) Object Type:\n   1) Animal\n   2) Building\n   3) Nature\n   4) Projectile\n   5) Structure\n   6) Unit")
		answer1 = int(input(": "))
		if answer1 == 1:
			inputPath = inputPath + "a"
		elif answer1 == 2:
			inputPath = inputPath + "b"
		elif answer1 == 3:
			inputPath = inputPath + "n"
		elif answer1 == 4:
			inputPath = inputPath + "p"
		elif answer1 == 5:
			inputPath = inputPath + "s"
		elif answer1 == 6:
			inputPath = inputPath + "u"
	answer2 = input("B) Type: ")
	answer3 = input("C) Name: ")
	hasAnim = True
	answer4 = input("D) Animation: ")
	if answer4 == "":
		hasAnim = False
	nImages = input("E) Number of Images: ")
	n = int(nImages)
	if hasAnim:
		inputPath = inputPath + "_" + answer2 + "_" + answer3 + "_" + answer4 + "_x1"
	else:
		inputPath = inputPath + "_" + answer2 + "_" + answer3 + "_x1"
	inputPath = inputPath + "\\" + inputPath + "_"

	nDeg = int(input("F) Number of Rotation degrees: "))
	print("G) Resulting Degrees:\n   1) 0º, 45º, 90º, 135º.. (8)\n   2) 45º, 90º, 135º, 180º.. (8)\n   3) All")
	degreesOption = int(input(": "))

	delLastFrame = int(input("G) Delete Last Frame?\n   1) YES\n   0) NO\n:"))

	numberStr = ""
	for i in range(n):
		numberStr = str(i + 1)
		while len(numberStr) < len(nImages) + 1:
			numberStr = "0" + numberStr
		
		# Image pixels changes
		inputImage = Image.open(inputPath + numberStr + ".bmp")
		inputImage_Mask = Image.open(inputPath + numberStr + "d.bmp")

		inWidth, inHeight = inputImage.size
		inWidth_m, inHeight_m = inputImage_Mask.size

		outputImage = Image.new('RGBA',(inWidth, inHeight))
		outputImage_m = Image.new('RGBA',(inWidth_m, inHeight_m))

		for x in range(inWidth):
			for y in range(inHeight):

				r, g, b = inputImage.getpixel((x,y))
				r_m, g_m, b_m = inputImage_Mask.getpixel((x,y))

				# Green or White Pixel (Unit Mask)
				if g_m > 150:
					outputImage.putpixel((x,y),inputImage.getpixel((x,y)))

					# Green Pixel(Unit Mask)
					if r_m == 0 and r_m == b_m:
						outputImage.putpixel((x,y),(255, 255, 255, 255))
						if b > 180:
							pixAlph = r
						else:
							pixAlph = 0
						outputImage_m.putpixel((x,y),(b, b, b, 255 - pixAlph))

					# White Pixel(Unit Mask)
					else:
						outputImage_m.putpixel((x,y),(0, 0, 0, 0))

				# Red or Magenta Pixel (Unit Mask)
				else:
					outputImage.putpixel((x,y),(0, 0, 0, 0))
					outputImage_m.putpixel((x,y),(0, 0, 0, 0))

		if hasAnim:
			outputPath = answer2 + "_" + answer3 + "_" + answer4 
		else:
			outputPath = answer2 + "_" + answer3

		if not os.path.exists(outputPath):
		   os.makedirs(outputPath)

		outputPath = outputPath + "\\" + outputPath

		if degreesOption == 1:
			if i + 1 != n or delLastFrame == 0:
				if (i + 1 > 0*((n - 1)/nDeg)) and (i + 1 <= 1*((n - 1)/nDeg)) or (i + 1 > 2*((n - 1)/nDeg)) and (i + 1 <= 3*((n - 1)/nDeg)) or (i + 1 > 4*((n - 1)/nDeg)) and (i + 1 <= 5*((n - 1)/nDeg))or (i + 1 > 6*((n - 1)/nDeg)) and (i + 1 <= 7*((n - 1)/nDeg)) or (i + 1 > 8*((n - 1)/nDeg)) and (i + 1 <= 9*((n - 1)/nDeg)) or (i + 1 > 10*((n - 1)/nDeg)) and (i + 1 <= 11*((n - 1)/nDeg)) or (i + 1 > 12*((n - 1)/nDeg)) and (i + 1 <= 13*((n - 1)/nDeg))or (i + 1 > 14*((n - 1)/nDeg)) and (i + 1 <= 15*((n - 1)/nDeg)):
					outputImage.save(outputPath + "_" + numberStr + ".bmp")
					outputImage_m.save(outputPath + "_Mask_" + numberStr + ".bmp")
		if degreesOption == 2:
			if i + 1 != n or delLastFrame == 0:
				if (i + 1 > 1*((n - 1)/nDeg)) and (i + 1 <= 2*((n - 1)/nDeg)) or (i + 1 > 3*((n - 1)/nDeg)) and (i + 1 <= 4*((n - 1)/nDeg)) or (i + 1 > 5*((n - 1)/nDeg)) and (i + 1 <= 6*((n - 1)/nDeg))or (i + 1 > 7*((n - 1)/nDeg)) and (i + 1 <= 8*((n - 1)/nDeg)) or (i + 1 > 9*((n - 1)/nDeg)) and (i + 1 <= 10*((n - 1)/nDeg)) or (i + 1 > 11*((n - 1)/nDeg)) and (i + 1 <= 12*((n - 1)/nDeg)) or (i + 1 > 13*((n - 1)/nDeg)) and (i + 1 <= 14*((n - 1)/nDeg))or (i + 1 > 15*((n - 1)/nDeg)) and (i + 1 <= 16*((n - 1)/nDeg)):
					outputImage.save(outputPath + "_" + numberStr + ".bmp")
					outputImage_m.save(outputPath + "_Mask_" + numberStr + ".bmp")
		elif degreesOption == 3:
			if i + 1 != n or n == 1 or delLastFrame == 0:
				outputImage.save(outputPath + "_" + numberStr + ".bmp")
				outputImage_m.save(outputPath + "_Mask_" + numberStr + ".bmp")
	it = it + 1
		