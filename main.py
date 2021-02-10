from tkinter import *
from tkinter import ttk
from classes import *
import pickle as pkl
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

#TAB 3 - Add Period
TAB3 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB3, text='Add Periods')

#TAB 4 - Add Teachers
TAB4 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB4, text='Add Teachers')

#TAB 5 - Add Learners
TAB5 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB5, text='Add Learners')

#TAB 6 - Add Plans
TAB6 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB6, text='Enter Learners')

#TAB 7 - Add Lessons
TAB7 = ttk.Frame(TAB_CONTROL)
TAB_CONTROL.add(TAB7, text='Enter Lessons')

#TAB Control - Add All Tabs
TAB_CONTROL.pack(expand=1, fill='both')

###SUBROUTINES###

#Enter Subject Details
def addsubject():
    #global subid
    x = Subject(subid.get(),subname.get(),faculty.get(),keystage.get())
    x.printall()
    subjects_data = []
    subjects_data.append(Subject(subid.get(),subname.get(),faculty.get(),keystage.get()))
    with open("subjects.p","wb") as subject_file:
        pkl.dump(subjects_data, subject_file)

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
    pkl.dump(acaclasses,fh)
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
    pkl.dump(periods,fh)
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
    pkl.dump(teachers,fh)
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
    pkl.dump(learners,fh)
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
    pkl.dump(plans,fh)
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
    pkl.dump(lessons,fh)
    fh.close()

#TAB1 Contents - Add Subject
ttk.Label(TAB1, text='Subject ID:').grid(column=0,row=0,padx=10,pady=10)
subid = StringVar()
ttk.Label(TAB1, text='Subject:').grid(column=0,row=1,padx=10,pady=10)
subname = StringVar()
ttk.Label(TAB1, text='Faculty:').grid(column=0,row=2,padx=10,pady=10)
faculty = StringVar()
ttk.Label(TAB1, text='Keystage:').grid(column=0,row=3,padx=10,pady=10)
keystage = StringVar()

ttk.Entry(TAB1,textvariable=subid).grid(column=1,row=0,padx=10,pady=10)
ttk.Entry(TAB1,textvariable=subname).grid(column=1,row=1,padx=10,pady=10)
ttk.Entry(TAB1,textvariable=faculty).grid(column=1,row=2,padx=10,pady=10)
ttk.Entry(TAB1,textvariable=keystage).grid(column=1,row=3,padx=10,pady=10)
ttk.Button(TAB1, text='Enter Details',command=lambda: addsubject()).grid(column=2,row=0,padx=10,pady=10)

#TAB2 Contents - Add Academic Class
ttk.Label(TAB2, text='Class ID:').grid(column=0,row=0,padx=10,pady=10)
classid = StringVar()
ttk.Label(TAB2, text='Subject:').grid(column=0,row=1,padx=10,pady=10) #Foreign Key
ttk.Label(TAB2, text='No. Pupils:').grid(column=0,row=2,padx=10,pady=10)
pupnum = StringVar()

ttk.Entry(TAB2,textvariable=classid).grid(column=1,row=0,padx=10,pady=10)
#ttk.Combobox(TAB2,) #Subject Lists
ttk.Entry(TAB2,textvariable=pupnum).grid(column=1,row=2,padx=10,pady=10)
ttk.Button(TAB2, text='Enter Details',command=lambda: addacaclass()).grid(column=2,row=0,padx=10,pady=10)

#TAB3 Contents - Add Periods


mainWin.mainloop()

###Global Variables###
#global subid
#subid = ""
#global classid
#classid = ""
global teacherid
teacherid = ""
global periodid
periodid = ""
global planid
planid = ""
global lessonid
lessonid = ""