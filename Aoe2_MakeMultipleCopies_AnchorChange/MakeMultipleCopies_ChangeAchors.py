from PIL import Image
import os

# CONSTANTS

# Repeated Trees
fileNames = []
fileNames.append("n_tree_acacia_x1")
fileNames.append("n_tree_autumn_oak_x1")
fileNames.append("n_tree_bamboo_x1")
fileNames.append("n_tree_baobab_x1")
fileNames.append("n_tree_bush_a_x1")
fileNames.append("n_tree_bush_b_x1")
fileNames.append("n_tree_bush_c_x1")
fileNames.append("n_tree_cypress_x1")
fileNames.append("n_tree_dead_x1")
fileNames.append("n_tree_dragon_x1")
fileNames.append("n_tree_italian_pine_x1")
fileNames.append("n_tree_jungle_x1")
fileNames.append("n_tree_mangrove_x1")
fileNames.append("n_tree_oak_x1")
fileNames.append("n_tree_olive_x1")
fileNames.append("n_tree_palm_x1")
fileNames.append("n_tree_pine_x1")
fileNames.append("n_tree_rainforest_x1")
fileNames.append("n_tree_reeds_x1")
fileNames.append("n_tree_snow_pine_x1")
fileNames.append("n_tree_snow_autumn_oak_x1")
# Number of variations
fileVar = []
fileVar.append(30)
fileVar.append(42)
fileVar.append(12)
fileVar.append(45)
fileVar.append(6)
fileVar.append(54)
fileVar.append(27)
fileVar.append(12)
fileVar.append(21)
fileVar.append(36)
fileVar.append(24)
fileVar.append(39)
fileVar.append(36)
fileVar.append(42)
fileVar.append(24)
fileVar.append(39)
fileVar.append(27)
fileVar.append(69)
fileVar.append(12)
fileVar.append(42)
fileVar.append(27)

# Original Images
imageName = 'tree_original'
imageMaskSuffix = 'd'

# Target Anchor
anchorValue = '75,106'

i = 0
while i < len(fileNames):

	inputPath = fileNames[i]

	# Copies
	n = fileVar[i]
	inputImage = Image.open(imageName + ".bmp")
	inputImage_d = Image.open(imageName + imageMaskSuffix + ".bmp")
	numberStr = ""

	for j in range(n):
		numberStr = str(j + 1)
		while len(numberStr) < len(str(n)) + 1:
			numberStr = "0" + numberStr
		inputImage.save(inputPath + "_" + numberStr + ".bmp")
		inputImage_d.save(inputPath + "_" + numberStr + imageMaskSuffix + ".bmp")

	# Anchor Change
	file1 = open(inputPath + '.slx', 'r')	
	Lines = file1.readlines()
	Lines2 = ''

	k = 1
	for line in Lines:
	    if k % 3 == 0:
	    	Lines2 = Lines2 + anchorValue + '\n'
	    else:
	    	Lines2 = Lines2 + line
	    k = k + 1
	file2 = open(inputPath + '_c' +'.slx', "w")
	file2.writelines(Lines2)


	i = i + 1
	


	