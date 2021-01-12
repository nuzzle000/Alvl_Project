#import tkinter
#import pickle
#from tkinter import tk
#mainWin = tkinter.Tk()
#mainWin.title("Untitled")
#mainWin.geometry("600x600")

#btn1 = tkinter.Button(mainWin, text="Hello").pack()

#mainWin.mainloop()

class Subject:
    def __init__(self,SubjectID,name,faculty,keystage):
        self.SubjectID = SubjectID
        self.name = name
        self.faculty = faculty
        self.keystage = keystage
    
class Class:
    def __init__(self,ClassID,SubjectID,numPups):
        self.ClassID = ClassID
        self.SubjectID = Subject(SubjectID)
        self.numpups = numpups


#
subid = 1234
inpname = input ("Name of subject ")
inpfaculty = input ("Enter Faculty ")
inpkeystage = input ("Enter Key Stage ")

subject = Subject(subid,inpname,inpfaculty,inpkeystage)
print (subject.name)