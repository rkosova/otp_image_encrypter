from PIL import Image, ImageDraw
class Encrypter():
	def __init__(self, plaintext, key):
		self.plaintext = plaintext
		self.key = key
		self.cipher = []


	def getEncrypted(self):
		return self.cipher


	def encrypt(self):
		for y in range(len(self.plaintext)):
			temp = []
			for x in range(len(self.plaintext[0])):
 				temp.append(((self.plaintext[y][x]+self.key[y][x]) % 2))
			self.cipher.append(temp)


	def drawEncrypted(self, path):
		im = Image.new("RGB", (len(self.cipher[0]), len(self.cipher)), (0, 0, 0))
		print(len(self.cipher[0]), len(self.cipher))
		drw = ImageDraw.Draw(im)
		for y in range(len(self.cipher)):
			for x in range(len(self.cipher[0])):
				if self.cipher[y][x] == 0:
					im.putpixel((x, y), (255, 255, 255))
				else:
					im.putpixel((x, y), (0, 0, 0))
		im.save(path+".png")
