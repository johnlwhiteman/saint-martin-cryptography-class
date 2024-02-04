from cryptography.fernet import Fernet
import os
import zlib

def compress(inputPath, outputPath):
  with open(inputPath, 'rb') as fd:
    inputText = fd.read()
  compressedText = zlib.compress(inputText, 2)
  with open(outputPath, 'wb') as fd:
    fd.write(compressedText)

def encrypt(inputPath, outputPath):
  key = Fernet.generate_key()
  crypto = Fernet(key)
  with open(inputPath, 'rb') as fd:
    plaintext = fd.read()
  ciphertext = crypto.encrypt(plaintext)
  with open(outputPath, 'wb') as fd:
    fd.write(ciphertext)

def runTest():

  # Compress then encrypt
  compress('plaintext.txt', 'compressed-plaintext.bin')
  encrypt('compressed-plaintext.bin', 'encrypted-compressed-plaintext.bin')
  compressThenEncryptStats = os.stat('encrypted-compressed-plaintext.bin')

  # Encrypt then compress
  encrypt('plaintext.txt', 'encrypted-plaintext.bin')
  compress('encrypted-plaintext.bin', 'compressed-encrypted-plaintext.bin')
  encryptThenCompressStats = os.stat('compressed-encrypted-plaintext.bin')

  # Print the stats
  print(f'\nCompress then encrypt: {compressThenEncryptStats.st_size} bytes')
  print(f'Encrypt then compress: {encryptThenCompressStats.st_size} bytes')
  print(f'{compressThenEncryptStats.st_size / encryptThenCompressStats.st_size * 100}%\n')

for i in range(0, 5):
  runTest()

