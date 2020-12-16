from PIL import Image, ImageDraw
class Decrypter():
    def __init__(self, cipher, key):
        self.cipher = cipher
        self.key = key
        self.plaintext = []


    def getDecrypted(self):
        return self.plaintext


    def decrypt(self):
        for y in range(len(self.cipher)):
            temp = []
            for x in range(len(self.cipher[0])):
                temp.append(((self.cipher[y][x]+self.key[y][x]) % 2))
                
            self.plaintext.append(temp)


    def drawDecrypted(self, path):
        im = Image.new("RGB", (len(self.plaintext[0]), len(self.plaintext)), (0, 0, 0))
        drw = ImageDraw.Draw(im)
        for y in range(len(self.plaintext)):
            for x in range(len(self.plaintext[0])):
                if self.plaintext[y][x] == 0:
                    im.putpixel((x, y), (255, 255, 255))
                else:
                    im.putpixel((x, y), (0, 0, 0))
            im.save(path+".png")


