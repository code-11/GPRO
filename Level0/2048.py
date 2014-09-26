import random

# game = True
up = -4
down = 4
left = -1
right = 1

# line1 = [0, 0, 0, 0]
# line2 = [0, 0, 0, 0]
# line3 = [0, 0, 0, 0]
# line4 = [0, 0, 0, 0]

# gameArray = line1 + line2 + line3 + line4

gameArray = [0,0,0,0,
			 0,0,0,0,
			 0,0,0,0,
			 0,0,0,0]

def setPrintArray(gameArray):
	line1 = gameArray[0:4]
	line2 = gameArray[4:8]
	line3 = gameArray[8:12]
	line4 = gameArray[12:16]
	printArray = [line1, line2, line3, line4]
	return printArray

def newBlockFunc(gameArray):
	zeroes = 0
	zeroesList = []
	for i in range(len(gameArray)):
		if gameArray[i] == 0:
			zeroes = zeroes + 1
			zeroesList.append(i)

	newBlockPos = random.choice(zeroesList)
	newBlock = 4 if random.randint(1,16) == 1 else 2
	return newBlockPos, newBlock

newBlockPos, newBlock = newBlockFunc(gameArray)
gameArray[newBlockPos] = newBlock
# print "a: ", newBlockPos, newBlock

while True:
	if 0 not in gameArray:
		print "Game Over!"
		# game = False
		break

	# zeroes = 0
	# zeroesList = []
	# for i in range(len(gameArray)):
	# 	if gameArray[i] == 0:
	# 		zeroes = zeroes + 1
	# 		zeroesList.append(i)

	# newBlockPos = random.choice(zeroesList)
	# newBlock = 4 if random.randint(1,16) == 1 else 2

	# break
	# if randint(1,32) == 1:
	# 	newBlock = 4
	# else:
	# 	newBlock = 2

	printArray = setPrintArray(gameArray)
	for line in printArray:
		print line

	try: 
		direction = input("Enter direction: ")
	except:
		print "Enter left, right, down, or up"


	for j in range(len(gameArray)):
		if gameArray[j] != 0:
			if gameArray[j + direction] == 0 and j + direction in range(len(gameArray)):
				print gameArray[j + direction]
				print gameArray[-3]
				print "something: ", j, j + direction
				# print element + direction
			# print element

	break

	# game = False

# print gameArray
# printArray = setPrintArray(gameArray)
# for line in printArray:
# 	print line