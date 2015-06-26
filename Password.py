__author__ = 'Abhishek'
from secret import Secret

import json
import os
import pickle


class Password():
    def __init__(self, date, password, cipherKey, encrypted=True):
        self.dateObj = date
        self.cipherKey = cipherKey
        if encrypted == False:
            self.password = self.__encryptPassword(password)
        else:
            self.password = password


    def __encryptPassword(self, plainText):
        s = Secret(self.cipherKey)
        return s.EncodeAES(plainText)

    def getPassword(self):
        s = Secret(self.cipherKey)
        return s.DecodeAES(self.password)

    def getDate(self):
        dateFormat = '%d-%m-%y'
        return self.dateObj.strftime(dateFormat)


    @staticmethod
    def addNewPassword(newPassword, fileName="data.pickle"):
        data = []
        with open(fileName, 'a+b') as handle:
            if not os.stat(fileName).st_size == 0:
                try:
                    data = pickle.load(handle)
                except EOFError:
                    handle.seek(0, 0)
            data.append(newPassword)
            handle.seek(0, 0)
            handle.truncate()
            handle.flush()
            pickle.dump(data, handle)


    @staticmethod
    def getAllPasswords(fileName="data.pickle"):
        data = []
        with open(fileName, 'a+b') as handle:
            if not os.stat(fileName).st_size == 0:
                try:
                    data = pickle.load(handle)
                except EOFError:
                    handle.seek(0, 0)
            return data





