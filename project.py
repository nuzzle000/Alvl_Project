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
global classid
classid = ""
global teacherid
teacherid = ""
global periodid
periodid = ""
global planid
planid = ""
global lessonid
lessonid = ""

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

class Lesson:
    def __init__(self,LessonID,Location,ClassID,SubjectID,TeacherID,PeriodID,PlanID):
        self.LessonID = LessonID
        self.Location = Location
        self.ClassID = ClassID
        self.SubjectID = SubjectID
        self.TeacherID = TeacherID
        self.PeriodID = PeriodID
        self.PlanID = PlanID
    def printall(self):
        print(self.LessonID, self.Location, self.ClassID, self.SubjectID, self.TeacherID, self.PeriodID, self.PlanID)

#Enter Subject Details
def addsubject():
    global subid
    subid = "1234" #Will be adjustable
    inpname = input ("Name of subject: ")
    inpfaculty = input ("Enter Faculty: ")
    inpkeystage = input ("Enter Key Stage: ")
    x = Subject(subid,inpname,inpfaculty,inpkeystage)
    x.printall()
    subjects = []
    subjects.append(Subject(subid,inpname,inpfaculty,inpkeystage))
    fh = open("subjects.p","wb")
    pickle.dump(subjects,fh)
    fh.close()


#Enter Class Details
def addacaclass():
    global inpclassid
    inpclassid = input ("Enter name of class eg.9Y1 : ")
    inpPup = input ("Number of pupils: ")
    x = AcademicClass(inpclassid,subid,inpPup)
    x.printall()
    acaclasses = []
    acaclasses.append(AcademicClass(inpclassid,subid,inpPup))
    fh = open("class.p","wb")
    pickle.dump(acaclasses,fh)
    fh.close()
    
    

#Enter Period Details
def addperiod():
    periodtime = ["0900","1000","1100","1200"] #Will be adjustable
    global periodid
    periodid = periodtime.index(input("Enter time of lesson: "))+1
    inpTOD = input("Enter time of day: ")
    inpDOW = input("Enter day of week: ")
    x = Period(periodid,inpTOD,inpDOW)
    x.printall()
    fh = open("period.p","wb")
    pickle.dump(periodid,fh)
    fh.close()

#Enter Teacher Details
def addteacher():
    global teacherid
    teacherid = "CMI" #Will be adjustable
    inpfirstname = input ("Enter teacher first name: ")
    inpsurname = input ("Enter teacher surname: ")
    x = Teacher(teacherid,inpsurname,inpfirstname)
    x.printall()
    fh = open("teachers.p","wb")
    pickle.dump(teacherid,fh)
    fh.close()

#Enter Learner Details
def addlearner():
    inpcustom1 = input("Enter custom information: ")
    learnerid="1234" #Will be adjustable
    x = Learner(learnerid,inpcustom1)
    x.printall()
    fh = open("learner.p","wb")
    pickle.dump(learnerid,fh)
    fh.close()
#Enter Plan Details
def addplan():
    global planid
    global lessonid
    planid = "1234" #Will be adjustable
    lessonid = "5678" #Will be adjustable
    inptext = input("Enter plan details: ")
    x = Plan(planid,lessonid,inptext)
    x.printall()
    fh = open("plan.p","wb")
    pickle.dump(planid,fh)
    fh.close()

#Enter Lesson Details
def addlesson():
    global lessonid
    lessonid = "1234" #Will be adjustable
    inplocation = input ("Enter lesson location: ")
    x = Lesson(lessonid,inplocation,classid,subid,teacherid,periodid,planid)
    x.printall()
    fh = open("lesson.p","wb")
    pickle.dump(lessonid,fh)
    fh.close()

#Testing
addsubject()
addacaclass()
addperiod()
addteacher()
addlearner()
addplan()
addlesson()