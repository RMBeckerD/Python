from PIL import Image
import os

iterations = int(input("Number of iterations: "))
it = 0
while it < iterations:
	inputPath = input("Input .slx file name: ")
	file1 = open(inputPath + '.slx', 'r')	
	Lines = file1.readlines()
	Lines2 = ''

	i = 1
	for line in Lines:
	    if i % 3 == 0:
	    	Lines2 = Lines2 +'48,83\n'
	    else:
	    	Lines2 = Lines2 + line
	    i = i + 1
	file2 = open(inputPath + '_c' +'.slx', "w")
	file2.writelines(Lines2)

	it = it + 1