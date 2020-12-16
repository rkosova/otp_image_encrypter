# otp_image_encrypter
This a simple python script that encrypts black and white images using a random key. This could, in theory, be used to encrypt images sent over a channel.

## HOW IT WORKS
The entire process is obviously based on the one time pad encryption technique, as in you can only use the key once per encryption and decryption after which it is best to use
a different key. This code, at it's current state, can only be used as a demonstration for one time encryptions and how encryption could look like for an image. However, the changes needed to turn it into a usable encryption/decryption tool are not too hard to make.
In its current state, this encryption works best with purely black and white images (as in images who contain only or mostly black and white) but can be used on images with color with which information retention is varied by the picture's composition. I am working on implementing RGB encryption in an efficient manner. 
### One Time Pad encryption
One Time pad encryption is a simple, tried and true method of encryption. The most basic conditions that are needed to be fulfilled for otp encryption to be successful:
* Both the encrypter and decrypter must *somehow* agree on the key,
* The key must be random and the same length as the message, and
* The key must not be used more than once.

If these rules are followed, the ecryption can be applied.
### OTP in this program
How the OTP in this program is applied is very simple:
1. First, the image to be encrypted is turned into a "text map" where 1 represents black (or here all hues > (127, 127, 127)) and 0 represents white (or here all hues < (127, 127, 127),
1. Second, a random key is generated witht the same dimensions as the **plaintext** (the text map of the image) and thus the same dimensions as the image (for now ;) ),
1. Third, the random key is applied to the plaintext to generate the **cipher**,
1. Fourth, the random key is then reapplied to the cipher to regenerate the plaintext.

Throughout all of this, a image representation of the encrypted text map and the decrypted text map is saved in the same directory as the code (you can change this in the code).

#### How the encryption is applied
Since we're basically encrypting binary values we use the modulo 2 addition operator on both the plaintext + key and the cipher + key. The modulo 2 addition operation has the same
truth table as XOR, i.e.,:

  0 + 0 = 0; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 0 
  
So, for every "bit" in the plain text there is a corresponding "bit" in the key that when added to each other, the value of that plaintext "bit" might change. This effectively creates noise. However, due to the properties of moudlo 2 addition, when the key is readded to the cipher the image decrypts. How this works is also simple:
 
 cipher + key = (plaintext + key) + key
               
 = plaintext + (key + key)
 
 = plaintext + 0 [in modulo 2 addition, when two bits of the same value are added the resulting bit is always 0]
               
