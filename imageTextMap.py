from PIL import Image
import sys
# convert image to black and white
class TextMap():
	def __init__(self, image):
		self.imageMatrix = []
		self.im = image
		self.width, self.height = self.im.size
		

	def getImageMatrix(self):
		return self.imageMatrix


	def matrixify(self, b_w_convert=True):
		
		if(b_w_convert): #checking here so it doesn't have to check every time per loop
			for y in range(self.height):
				temp = []
				for x in range(self.width):
					if self.im.getpixel((x, y)) > (128, 128, 128):
						temp.append(0)
					else:
						temp.append(1)
				self.imageMatrix.append(temp)						
		else:
			for y in range(self.height):
				temp = []
				for x in range(self.width):
					if im.getpixel((x, y)) == (255, 255, 255) or im.getpixel((x, y)) > (0, 0, 0):# this is designed to remove grays
						temp.append(0)
					else:
						temp.append(1)
				self.imageMatrix.append(temp)	


