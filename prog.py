from Crypto.Cipher import AES
import base64
import sys
import os
from Password import Password
from datetime import datetime
import pickle


dateFormat = '%d-%m-%y %H:%M'

BLOCK_SIZE = 32

PADDING = "{"


def pad(s):
    return s + (BLOCK_SIZE - (len(s) % BLOCK_SIZE)) * PADDING  # return a padded string
    # take the length of the string, mod it by block size and then add the padding ({) no. of times the block_size - (mod)


def EncodeAES(plaintext, cipher):
    return cipher.encrypt(pad(plaintext))


def DecodeAES(cipherText, cipher):
    return cipher.decrypt(cipherText).rstrip(PADDING)


# secret = os.urandom(BLOCK_SIZE)
#
# cipher = AES.new(secret)
#
# encoded = EncodeAES("This my string", cipher)
#
# print encoded
#
# decoded = DecodeAES(encoded, cipher)
#
# print decoded



def printMenu():
    print "1. Enter a new password"
    print "2. Show all passwords"
    print "3. Clear the file"


def entertainChoice(choice):
    if choice == "1":
        date = raw_input("Enter date (dd-mm-yy H:M): ")

        try:
            date = datetime.strptime(date, dateFormat)
        except ValueError:
            print "Date not correct. Try again."
            sys.exit(0)
        password = raw_input("Enter password: ")
        cipherKey = os.urandom(32)
        p = Password(date, password, cipherKey, encrypted=False)
        Password.addNewPassword(p)


    elif choice == "2":
        data = Password.getAllPasswords()
        todayDate = datetime.now()
        if len(data) == 0:
            print "File seems to be empty"
        else:
            for counter, p in enumerate(data):
                if todayDate >= p.dateObj:
                    print "{0}. date: {1} \t password: {2}".format(counter, p.getDate(), p.getPassword())
                else:
                    print "Password will be available on/from: {0}".format(p.getDate())

    elif choice == "3":
        confirm = raw_input("Are you sure? y/n")
        if( confirm == 'y'):
            Password.clearAllPasswords()
        else:
            return




def main():
    try:
        while True:
            printMenu()
            choice = raw_input("Choose: ")
            entertainChoice(choice)
    except KeyboardInterrupt:
        print "Goodbye!"


if __name__ == "__main__":
    main()
    # with open('data.pickle','a+b') as handle:
        # print pickle.load(handle)
        # print pickle.load(handle)
        # handle.truncate()
