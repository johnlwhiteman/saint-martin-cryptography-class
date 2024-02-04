from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from PIL import Image
from pathlib import Path
import os

BLOCK_SIZE = 32
HEADER_SIZE = 64

def encryptAsAesEcb(inputPath, outputPath):
  tmpImgPath = f'{Path(inputPath).stem}-aes-ecb-tmpy.bmp'
  Image.open(inputPath).save(tmpImgPath)
  key = get_random_bytes(16)
  cipher = AES.new(key, AES.MODE_ECB)
  with open(tmpImgPath, mode='rb') as fd:
    plaintext = fd.read()
  _boundary = len(plaintext) % 16
  _plaintext = plaintext[HEADER_SIZE:-_boundary]
  ciphertext = cipher.encrypt(pad(_plaintext, BLOCK_SIZE))
  ciphertext = plaintext[0:HEADER_SIZE] + ciphertext + plaintext[-_boundary:]
  with open(tmpImgPath, "wb") as file:
    file.write(ciphertext)
  Image.open(tmpImgPath).save(outputPath)
  os.unlink(tmpImgPath)

def encryptAsAesCbc(inputPath, outputPath):
  tmpImgPath = f'{Path(inputPath).stem}-aes-cbc-tmpy.bmp'
  Image.open(inputPath).save(tmpImgPath)
  key = get_random_bytes(16)
  iv = get_random_bytes(16)
  cipher = AES.new(key, AES.MODE_CBC, iv)
  with open(tmpImgPath, mode='rb') as fd:
    plaintext = fd.read()
  _boundary = len(plaintext) % 16
  _plaintext = plaintext[HEADER_SIZE:-_boundary]
  ciphertext = cipher.encrypt(pad(_plaintext, BLOCK_SIZE))
  ciphertext = plaintext[0:HEADER_SIZE] + ciphertext + plaintext[-_boundary:]
  with open(tmpImgPath, "wb") as file:
    file.write(ciphertext)
  Image.open(tmpImgPath).save(outputPath)
  os.unlink(tmpImgPath)


encryptAsAesEcb('tux.png', 'tux-aes-ecb.png')
encryptAsAesCbc('tux.png', 'tux-aes-cbc.png')

encryptAsAesEcb('smu.png', 'smu-aes-ecb.png')
encryptAsAesCbc('smu.png', 'smu-aes-cbc.png')

encryptAsAesEcb('007.png', '007-aes-ecb.png')
encryptAsAesCbc('007.png', '007-aes-cbc.png')