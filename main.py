from tkinter import *
from tkinter import ttk
from classes import *
import pickle as pkl


#Logout
def logout():
    mainWin.destroy()

mainWin = Tk()
mainWin.title("Teacher Planner")
mainWin.geometry("600x600")
Button(mainWin, text="Logout", command=logout).pack()
#mainWin.PhotoImage(file="logo.ico")

#TAB Control (Parent)
TAB_CONTROL_MAIN = ttk.Notebook(mainWin)
TAB8 = ttk.Frame(TAB_CONTROL_MAIN)
TAB9 = ttk.Frame(TAB_CONTROL_MAIN)
TABX = ttk.Frame(TAB_CONTROL_MAIN)

TAB_CONTROL_ADD = ttk.Notebook(TAB8)

#TAB 8 - Add Details
TAB_CONTROL_MAIN.add(TAB8, text='Add Details')

#TAB 9 - View Details
TAB_CONTROL_MAIN.add(TAB9, text='View Details')

#TAB X - Settings
TAB_CONTROL_MAIN.add(TABX, text='Settings')

#TAB 1 - Add Subject
TAB1 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB1, text='Add Subject')

#TAB 2 - Add Academic Class
TAB2 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB2, text='Add Class')

#TAB 3 - Add Period
TAB3 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB3, text='Add Periods')

#TAB 4 - Add Teachers
TAB4 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB4, text='Add Teachers')

#TAB 5 - Add Learners
TAB5 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB5, text='Add Learners')

#TAB 6 - Add Plans
TAB6 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB6, text='Add Plans')

#TAB 7 - Add Lessons
TAB7 = ttk.Frame(TAB_CONTROL_ADD)
TAB_CONTROL_ADD.add(TAB7, text='Add Lessons')


#TAB Control - Add Tabs
TAB_CONTROL_ADD.pack(expand=1, fill='both')
TAB_CONTROL_MAIN.pack(expand=1, fill='both')



###SUBROUTINES###

#Enter Subject Details
def addsubject():
    #global subid
    x = Subject(subid.get(),subname.get(),faculty.get(),keystage.get())
    x.printall()
    subjects_data = []
    subjects_data.append(x)
    fh = open("subjects.p","wb")
    pkl.dump(subjects_data,fh)
    fh.close()
#Enter Class Details
def addacaclass():
    global inpclassid
    inpclassid = input ("Enter name of class eg.9Y1 : ")
    inpPup = input ("Number of pupils: ")
    x = AcademicClass(inpclassid,subid,inpPup)
    x.printall()
    acaclasses_data = []
    acaclasses_data.append(x)
    fh = open("acaclasses.p","wb")
    pkl.dump(acaclasses_data,fh)
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
    periods_data = []
    periods_data.append(x)
    fh = open("periods.p","wb")
    pkl.dump(periods_data,fh)
    fh.close()

#Enter Teacher Details
def addteacher():
    global teacherid
    teacherid = "CMI" #Will be adjustable
    inpfirstname = input ("Enter teacher first name: ")
    inpsurname = input ("Enter teacher surname: ")
    x = Teacher(teacherid,inpsurname,inpfirstname)
    x.printall()
    teachers_data = []
    teachers_data.append(x)
    fh = open("teachers.p","wb")
    pkl.dump(teachers_data,fh)
    fh.close()

#Enter Learner Details
def addlearner():
    inpcustom1 = input("Enter custom information: ")
    learnerid="1234" #Will be adjustable
    x = Learner(learnerid,inpcustom1)
    x.printall()
    learners_data = []
    learners_data.append(x)
    fh = open("learners.p","wb")
    pkl.dump(learners_data,fh)
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
    plans_data = []
    plans_data.append(x) 
    fh = open("plans.p","wb")
    pkl.dump(plans_data,fh)
    fh.close()

#Enter Lesson Details
def addlesson():
    global lessonid
    lessonid = "1234" #Will be adjustable
    inplocation = input ("Enter lesson location: ")
    x = Lesson(lessonid,inplocation,classid,subid,teacherid,periodid,planid)
    x.printall()
    lessons_data = []
    lessons_data.append(x) 
    fh = open("lessons.p","wb")
    pkl.dump(lessons_data,fh)
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
try: #IMPROVE
    with open("subjects.p","rb") as subject_file:
        data = pkl.load(subject_file)
except:
    pass
ttk.Label(TAB2, text='Class ID:').grid(column=0,row=0,padx=10,pady=10)
classid = StringVar()
ttk.Label(TAB2, text='Subject:').grid(column=0,row=1,padx=10,pady=10) #Foreign Key
ttk.Label(TAB2, text='No. Pupils:').grid(column=0,row=2,padx=10,pady=10)
pupnum = StringVar()

ttk.Entry(TAB2,textvariable=classid).grid(column=1,row=0,padx=10,pady=10)
acaclass_sub = StringVar() 
sub_data = ttk.Combobox(TAB2,textvariable=acaclass_sub) 
sub_data['values'] = (data) 
sub_data.grid(column=1,row=1,padx=10,pady=10) 
sub_data.current() 
ttk.Entry(TAB2,textvariable=pupnum).grid(column=1,row=2,padx=10,pady=10)
ttk.Button(TAB2, text='Enter Details',command=lambda: addacaclass()).grid(column=2,row=0,padx=10,pady=10)

#TAB3 Contents - Add Periods
ttk.Label(TAB3, text='Time of Period:').grid(column=0,row=0,padx=10,pady=10)
periodid = StringVar()
ttk.Label(TAB3, text='Week Day:').grid(column=0,row=1,padx=10,pady=10)
DOW = StringVar()

ttk.Entry(TAB3,textvariable=periodid).grid(column=1,row=0,padx=10,pady=10)
ttk.Entry(TAB3,textvariable=DOW).grid(column=1,row=1,padx=10,pady=10)
ttk.Button(TAB3, text='Enter Details',command=lambda: addperiod()).grid(column=2,row=0,padx=10,pady=10)

#TAB4 Contents - Add Teacher Details
ttk.Label(TAB4, text='First Name:').grid(column=0, row=0, padx=10, pady=10)
FN = StringVar()
ttk.Label(TAB4, text='Last Name:').grid(column=0, row=1, padx=10, pady=10)
SN = StringVar()

ttk.Entry(TAB4, textvariable=FN).grid(column=1, row=0, padx=10, pady=10)
ttk.Entry(TAB4, textvariable=SN).grid(column=1, row=1, padx=10, pady=10)
ttk.Button(TAB4, text='Enter Details').grid(column=2,row=0,padx=10,pady=10)

#TAB5 Contents - Add Learner Details
ttk.Label(TAB5, text='Learner ID:').grid(column=0,row=0,padx=10,pady=10)
LearnerID = StringVar()
ttk.Label(TAB5, text='Details:').grid(column=0,row=1,padx=10,pady=10)
LearnerDet = StringVar()

ttk.Entry(TAB5, textvariable=LearnerID).grid(column=1,row=0,padx=10,pady=10)
Text(TAB5).grid(column=1,row=1,padx=50,pady=10)


mainWin.mainloop()

###Global Variables###
#global subid
#subid = ""
#global classid
#classid = ""
#global periodid
#periodid = ""
global teacherid
teacherid = ""
global planid
planid = ""
global lessonid
lessonid = ""