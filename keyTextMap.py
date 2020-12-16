import random 
from PIL import Image

'''
One idea for random number generation for the key is
to create a Pseudo RNG algorithm such that all generated
numbers are deterministic and reproducable 
given a starting nu,ber/sequence and equip the encrypter
and decrypter with the algorithm. Thus the channel only 
has to send the first numer/sequence and the decrypter 
can use that number/sequence to regenerate the key 
for decryption. It has to be secure and with a hard to 
crack pattern for use in real cryptographic problems
but in our case a simple one should do fine	
'''
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






