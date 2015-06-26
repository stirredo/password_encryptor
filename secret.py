__author__ = 'Abhishek'

from Crypto.Cipher import AES

class Secret():
    def __init__(self, key, BLOCK_SIZE = 32, PADDING = "{"):
        self.BLOCK_SIZE = 32
        self.PADDING = "{"
        self.cipher = AES.new(key)

    def pad(self, s):
        return s + (self.BLOCK_SIZE - (len(s) % self.BLOCK_SIZE)) * self.PADDING # return a padded string
        #take the length of the string, mod it by block size and then add the padding ({) no. of times the block_size - (mod)

    def EncodeAES(self, plaintext):
        return self.cipher.encrypt(self.pad(plaintext))

    def DecodeAES(self, cipherText):
        return self.cipher.decrypt(cipherText).rstrip(self.PADDING)


