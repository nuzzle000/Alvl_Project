#import tkinter
#import pickle
#from tkinter import tk
#mainWin = tkinter.Tk()
#mainWin.title("Untitled")
#mainWin.geometry("600x600")

#btn1 = tkinter.Button(mainWin, text="Hello").pack()

#mainWin.mainloop()

#Creating classes for information storage
class Subject:
    def __init__(self,SubjectID,name,faculty,keystage):
        self.SubjectID = SubjectID
        self.name = name
        self.faculty = faculty
        self.keystage = keystage
    
class Class:
    def __init__(self,ClassID,SubjectID,numPups):
        self.ClassID = ClassID
        self.SubjectID = SubjectID
        self.numPups = numPups


#Enter Subject Details
subid = "1234"
inpname = input ("Name of subject: ")
inpfaculty = input ("Enter Faculty ")
inpkeystage = input ("Enter Key Stage ")

x = Subject(subid,inpname,inpfaculty,inpkeystage)

print (x.name + " was entered successfully")
print (x.SubjectID + " was entered successfully")
print (x.faculty + " was entered successfully")
print (x.keystage + " was entered successfully")

#Enter Class Details
classid = "9Y1"
inpPup = input ("Number of pupils: ")
y = Class(classid,subid,inpPup)

print (y.ClassID + " was entered successfully")
print (y.SubjectID + " was entered successfully")
print (y.numPups + " was entered successfully")
