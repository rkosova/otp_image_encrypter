from PIL import Image, ImageDraw
import sys
import random
import imageTextMap, keyTextMap, binaryOnePadEncrypter, binaryOnePadDecrypter

pathToImage = sys.argv[1]
pathToSaveEnc = sys.argv[2]
pathToSaveDec = sys.argv[3]
im = Image.open(pathToImage)

tMap = imageTextMap.TextMap(im)
kMap = keyTextMap.KeyMap(im.size)
cMap = binaryOnePadEncrypter.Encrypter(tMap.getImageMatrix(), kMap.getKeyMatrix())
dMap = binaryOnePadDecrypter.Decrypter(cMap.getEncrypted(), kMap.getKeyMatrix())
tMap.matrixify()
kMap.generateKeyMatrix()
cMap.encrypt()
cMap.drawEncrypted(pathToSaveEnc)
dMap.decrypt()
dMap.drawDecrypted(pathToSaveDec)
