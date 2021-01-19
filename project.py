#import tkinter
import pickle
#from tkinter import tk
#mainWin = tkinter.Tk()
#mainWin.title("Untitled")
#mainWin.geometry("600x600")

#btn1 = tkinter.Button(mainWin, text="Hello").pack()

#mainWin.mainloop()

#Global Variables
global subid
subid = ""

#Creating classes for information storage
class Subject:
    def __init__(self,SubjectID,name,faculty,keystage):
        self.SubjectID = SubjectID
        self.name = name
        self.faculty = faculty
        self.keystage = keystage
    def printall(self):
        print(self.SubjectID, self.name, self.faculty, self.keystage)
    
class AcademicClass:
    def __init__(self,ClassID,SubjectID,numPups):
        self.ClassID = ClassID
        self.SubjectID = SubjectID
        self.numPups = numPups
    def printall(self):
        print(self.ClassID, self.SubjectID, self.numPups)

class Period:
    def __init__(self,PeriodID,TOD,DOW):
        self.PeriodID = PeriodID
        self.TOD = TOD
        self.DOW = DOW
    def printall(self):
        print(self.PeriodID, self.TOD, self.DOW)

class Teacher:
    def __init__(self,TeacherID,surname,firstname):
        self.TeacherID = TeacherID
        self.surname = surname
        self.firstname = firstname
    def printall(self):
        print(self.TeacherID, self.surname, self.firstname)

class Learner:
    def __init__(self,LearnerID,Custom1):
        self.LearnerID = LearnerID
        self.Custom1 = Custom1
    def printall(self):
        print(self.LearnerID, self.Custom1)

class Plan:
    def __init__(self,PlanID,LessonID,Text):
        self.PlanID = PlanID
        self.LessonID = LessonID
        self.Text = Text
    def printall(self):
        print(self.PlanID, self.LessonID, self.Text)

#Enter Subject Details
def addsubject():
    subid = "1234"
    inpname = input ("Name of subject: ")
    inpfaculty = input ("Enter Faculty: ")
    inpkeystage = input ("Enter Key Stage: ")
    x = Subject(subid,inpname,inpfaculty,inpkeystage)
    x.printall()

#Enter Class Details
def addacaclass():
    classid = "9Y1"
    inpPup = input ("Number of pupils: ")
    x = AcademicClass(classid,subid,inpPup)
    x.printall()

#Enter Period Details
def addperiod():
    periodid = "1"
    inpTOD = input("Enter time of day: ")
    inpDOW = input("Enter day of week: ")
    x = Period(periodid,inpTOD,inpDOW)
    x.printall()

#Enter Teacher Details
def addteacher():
    teacherid = "CMI"
    inpfirstname = input ("Enter teacher first name: ")
    inpsurname = input ("Enter teacher surname: ")
    x = Teacher(teacherid,inpsurname,inpfirstname)
    x.printall()

#Enter Learner Details
def addlearner():
    inpcustom1 = input("Enter custom information: ")
    learnerid="1234"
    x = Learner(learnerid,inpcustom1)
    x.printall()

#Enter Plan Details
def addplan():
    planid = "1234"
    lessonid = "5678"
    inptext = input("Enter plan details: ")
    x = Plan(planid,lessonid,inptext)
    x.printall()