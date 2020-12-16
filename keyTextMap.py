import random 
from PIL import Image

#for now we use random.randint
class KeyMap():
	def __init__(self, imageSize):
		self.width, self.height = imageSize
		self.keyMatrix = []


	def getKeyMatrix(self):
		return self.keyMatrix


	def generateKeyMatrix(self):
		for y in range(self.height):
			temp = []
			for x in range(self.width):
				if random.randint(0, 9) >= 5:
					temp.append(1)
				else:
					temp.append(0)
			self.keyMatrix.append(temp)


