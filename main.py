from tkinter import *
from tkinter import ttk
from classes import *
import pickle
mainWin = Tk()
mainWin.title("Teacher Planner")
mainWin.geometry("600x600")
Button(mainWin, text="Logout").pack()

#TAB Control (Parent)
TAB_CONTROL = ttk.Notebook(mainWin)

#TAB 1 - Add Subject
TAB1 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB1, text='Add Subject')

#TAB 2 - Add Academic Class
TAB2 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB2, text='Add Class')

#TAB Control - Add All Tabs
TAB_CONTROL.pack(expand=1, fill='both')

###SUBROUTINES###

#Enter Subject Details
def addsubject():
    global subid
    subid = "1234" #Will be adjustable
    inpfaculty = input ("Enter Faculty: ")
    inpkeystage = input ("Enter Key Stage: ")
    x = Subject(subid,subname.get(),inpfaculty,inpkeystage)
    x.printall()
    subjects = []
    subjects.append(Subject(subid,subname.get(),inpfaculty,inpkeystage))
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
    fh = open("classes.p","wb")
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
    periods = []
    periods.append(Period(periodid,inpTOD,inpDOW))
    fh = open("periods.p","wb")
    pickle.dump(periods,fh)
    fh.close()

#Enter Teacher Details
def addteacher():
    global teacherid
    teacherid = "CMI" #Will be adjustable
    inpfirstname = input ("Enter teacher first name: ")
    inpsurname = input ("Enter teacher surname: ")
    x = Teacher(teacherid,inpsurname,inpfirstname)
    x.printall()
    teachers = []
    teachers.append(Teacher(teacherid,inpsurname,inpfirstname))
    fh = open("teachers.p","wb")
    pickle.dump(teachers,fh)
    fh.close()

#Enter Learner Details
def addlearner():
    inpcustom1 = input("Enter custom information: ")
    learnerid="1234" #Will be adjustable
    x = Learner(learnerid,inpcustom1)
    x.printall()
    learners = []
    learners.append(Learner(learnerid,inpcustom1))
    fh = open("learners.p","wb")
    pickle.dump(learners,fh)
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
    plans = []
    plans.append(Plan(planid,lessonid,inptext)) 
    fh = open("plans.p","wb")
    pickle.dump(plans,fh)
    fh.close()

#Enter Lesson Details
def addlesson():
    global lessonid
    lessonid = "1234" #Will be adjustable
    inplocation = input ("Enter lesson location: ")
    x = Lesson(lessonid,inplocation,classid,subid,teacherid,periodid,planid)
    x.printall()
    lessons = []
    lessons.append(Lesson(lessonid,inplocation,inpclassid,subid,teacherid,periodid,planid)) 
    fh = open("lessons.p","wb")
    pickle.dump(lessons,fh)
    fh.close()

#TAB Contents
ttk.Label(TAB1, text='Name of Subject:').grid(column=0,row=0,padx=10,pady=10)
subname = StringVar()
#subname.set("")
ttk.Entry(TAB1,textvariable=subname).grid(column=1,row=0,padx=10,pady=10)
ttk.Button(TAB1, text='Test Button',command=lambda: addsubject()).grid(column=2,row=0,padx=10,pady=10)

mainWin.mainloop()

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