from tkinter import *
from tkinter import ttk, filedialog, messagebox
from classes import *
import pickle as pkl
import subprocess
import datetime as dt


#Logout
def logout():
    mainWin.destroy()

mainWin = Tk()
mainWin.title("Teacher Planner")
mainWin.geometry("650x600")
Button(mainWin, text="Logout", command=logout).pack()
#mainWin.PhotoImage(file="logo.ico")

def BubbleSort():
    n = len(data) # Gets length of array
    Sort = False
    while n != 1: #While length is not reduced to 1:
        print("***",data)
        for i in range (0, n-1):
            print(data)
            if data[i] > data[i + 1]: #Comparing 2 bits of data in array
                Temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = Temp
                Sort = True
        n = n - 1 #Reduce length to be sorted by 1
    if Sort == True:
        print(data)

def BinSrcRecursive(data,SearchItem):
    BubbleSort()
    Start = 0
    End = int(len(data))-1
    SearchItem = int(input("What do you want to find?"))
    def Search(data, SearchItem):

        Middle = (Start + End)//2
        if data[Middle] == SearchItem:
            print("Found")
        else:
            Search(data, SearchItem)

    Search(data, SearchItem)

# TAB Control (Parent)
TAB_CONTROL_MAIN = ttk.Notebook(mainWin)
TAB8 = ttk.Frame(TAB_CONTROL_MAIN)
TAB9 = ttk.Frame(TAB_CONTROL_MAIN)
TABX = ttk.Frame(TAB_CONTROL_MAIN)

TAB_CONTROL_ADD = ttk.Notebook(TAB8)
TAB_CONTROL_VIEW = ttk.Notebook(TAB9)

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

#TAB 10 - View Time Table 
TAB10 = ttk.Frame(TAB_CONTROL_VIEW)
TAB_CONTROL_VIEW.add(TAB10, text='View Time Table')


#TAB Control - Add Tabs
TAB_CONTROL_ADD.pack(expand=1, fill='both')
TAB_CONTROL_MAIN.pack(expand=1, fill='both')
TAB_CONTROL_VIEW.pack(expand=1, fill='both')


###SUBROUTINES

#Enter Subject Details
def addsubject():
    try:
        fh = open('subjects.p','rb')
        data = pkl.load(fh)
        fh.close()
        subid = data[-1].SubjectID + 1
    except FileNotFoundError:
        subid = 0000
    
    x = Subject(subid,subname.get(),faculty.get(),keystage.get())
    valid = True
    errormsg = ""
    
    if subname.get() == "":
        valid = False
        errormsg += ("Please enter a Subject Name")
    if len(subname.get()) <= 16:
        valid = False
        errormsg += ("Max character limit for subject is 16")
    if subname.get().isalpha():
        valid = False
        errormsg += ("Please enter only letters")

        try:
            fh = open('subjects.p','rb')
            data = pkl.load(fh)
            fh.close()
            print(data)
            data.append(x)
            print(data)
            fh = open('subjects.p','wb')
            pkl.dump(data,fh)
            fh.close()
        except FileNotFoundError:
            fh = open('subjects.p','wb')
            pkl.dump([x],fh)
            print(fh)
            fh.close()
    else:
        messagebox.showinfo(title="oh no", message="numb 'ed")

#Enter Class Details
def addacaclass():
    x = AcademicClass(AcaClassID.get(),SubjectID.get(),pupnum.get())
    try:
        fh = open('acalasses.p','rb')
        data = pkl.load(fh)
        fh.close()
        print(data)
        data.append([x])
        print(data)
        fh = open('acalasses.p','wb')
        pkl.dump(data,fh)
        fh.close()
    except FileNotFoundError:
        fh = open('acalasses.p','wb')#fh = open('subjects.p','rb')
    #data = pkl.load(fh)
    #fh.close()
    #print (data[-1])
        pkl.dump(x,fh)
        print(fh)
        fh.close()
    
#Enter Period Details
def addperiod():
    periodtime = ["0900","1000","1100","1200"] #Will be adjustable
    x = Period(periodid.get(),inpTOD,DOW.get())
    try:
        fh = open('periods.p','rb')
        data = pkl.load(fh)
        fh.close()
        print(data)
        data.append([x])
        print(data)
        fh = open('periods.p','wb')
        pkl.dump(data,fh)
        fh.close()
    except FileNotFoundError:
        fh = open('periods.p','wb')
        pkl.dump(x,fh)
        print(fh)
        fh.close()

#Enter Teacher Details
def addteacher():
    teacherid = "CMI" #Will be adjustable
    x = Teacher(TeacherID.get(),SN.get(),FN.get())
    try:
        fh = open('teachers.p','rb')
        data = pkl.load(fh)
        fh.close()
        print(data)
        data.append([x])
        print(data)
        fh = open('teachers.p','wb')
        pkl.dump(data,fh)
        fh.close()
    except FileNotFoundError:
        fh = open('teachers.p','wb')
        pkl.dump(x,fh)
        print(fh)
        fh.close()

#Enter Learner Details
def addlearner():
    x = Learner(LearnerID.get(),LearnerDet.get())
    try:
        fh = open('learners.p','rb')
        data = pkl.load(fh)
        fh.close()
        print(data)
        data.append([x])
        print(data)
        fh = open('learners.p','wb')
        pkl.dump(data,fh)
        fh.close()
    except FileNotFoundError:
        fh = open('learners.p','wb')
        pkl.dump(x,fh)
        print(fh)
        fh.close()

#Enter Plan Details
def addplan():
    lessonid = "5678" #Will be adjustable
    #path = filedialog.askopenfilename()
    x = Plan(PlanID.get(),lessonid,PlanDet.get())
    try:
        fh = open('plans.p','rb')
        data = pkl.load(fh)
        fh.close()
        print(data)
        data.append([x])
        print(data)
        fh = open('plans.p','wb')
        pkl.dump(data,fh)
        fh.close()
    except FileNotFoundError:
        fh = open('plans.p','wb')
        pkl.dump(x,fh)
        print(fh)
        fh.close()
        
def addplanfile():
    path = filedialog.askopenfilename()
    print(path)

#Enter Lesson Details
def addlesson():
    lessonid = "1234" #Will be adjustable
    x = Lesson(lessonid,LocationID.get(),AcaClassID.get(),SubjectID.get(),TeacherID.get(),periodid.get(),PlanID.get())
    try:
        fh = open('lessons.p','rb')
        data = pkl.load(fh)
        fh.close()
        print(data)
        data.append(x)
        print(data)
        fh = open('lessons.p','wb')
        pkl.dump(data,fh)
        fh.close()
    except FileNotFoundError:
        fh = open('lessons.p','wb')
        pkl.dump([x],fh)
        print(fh)
        fh.close()

#View TimeTable
def viewtimetable():
    pass

#TAB1 Contents - Add Subject

#ttk.Label(TAB1, text='Subject ID:').grid(column=0,row=0,padx=10,pady=10)
#subid = StringVar()
ttk.Label(TAB1, text='Subject:').grid(column=0,row=0,padx=10,pady=10)
subname = StringVar()
ttk.Label(TAB1, text='Faculty:').grid(column=0,row=1,padx=10,pady=10)
faculty = StringVar()
ttk.Label(TAB1, text='Keystage:').grid(column=0,row=2,padx=10,pady=10)
keystage = StringVar()

#ttk.Entry(TAB1,textvariable=subid).grid(column=1,row=0,padx=10,pady=10)
ttk.Entry(TAB1,textvariable=subname).grid(column=1,row=0,padx=10,pady=10)
ttk.Entry(TAB1,textvariable=faculty).grid(column=1,row=1,padx=10,pady=10)
ttk.Entry(TAB1,textvariable=keystage).grid(column=1,row=2,padx=10,pady=10)
ttk.Button(TAB1, text='Enter Details',command=lambda: addsubject()).grid(column=2,row=0,padx=10,pady=10)

#TAB2 Contents - Add Academic Class
try: #IMPROVE
    with open("subjects.p","rb") as subject_file:
        data = pkl.load(subject_file)
except:
    data = []
ttk.Label(TAB2, text='Class ID eg. 9/Y1:').grid(column=0,row=0,padx=10,pady=10)
classid = StringVar()
ttk.Label(TAB2, text='Subject:').grid(column=0,row=1,padx=10,pady=10) #Foreign Key
ttk.Label(TAB2, text='No. Pupils:').grid(column=0,row=2,padx=10,pady=10)
pupnum = StringVar()

ttk.Entry(TAB2,textvariable=classid).grid(column=1,row=0,padx=10,pady=10)
acaclass_sub = StringVar() 
sub_data = ttk.Combobox(TAB2,textvariable=acaclass_sub)

#Extracting Subject names into separate list
displaydata = []
for item in data:
    displaydata.append(item.name)
sub_data['values'] = displaydata
 
sub_data.grid(column=1,row=1,padx=10,pady=10) 
sub_data.current() 
ttk.Entry(TAB2,textvariable=pupnum).grid(column=1,row=2,padx=10,pady=10)
ttk.Button(TAB2, text='Enter Details',command=lambda: addacaclass()).grid(column=2,row=0,padx=10,pady=10)

#TAB3 Contents - Add Periods
ttk.Label(TAB3, text='Time of Day:').grid(column=0,row=0,padx=10,pady=10)
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
ttk.Button(TAB4, text='Enter Details',command=lambda: addteacher()).grid(column=2,row=0,padx=10,pady=10)

#TAB5 Contents - Add Learner Details
ttk.Label(TAB5, text='Learner ID:').grid(column=0,row=0,padx=10,pady=10)
LearnerID = StringVar()
ttk.Label(TAB5, text='Details:').grid(column=0,row=1,padx=10,pady=10)
LearnerDet = StringVar()

ttk.Entry(TAB5, textvariable=LearnerID).grid(column=1,row=0,padx=10,pady=10)
Text(TAB5, width=50, height=20, wrap=WORD).grid(column=1,row=1,padx=10,pady=10)
ttk.Button(TAB5, text='Enter Details',command=lambda: addlearner()).grid(column=2,row=0,padx=10,pady=10)

#TAB6 Contents - Add Plan Details
ttk.Label(TAB6, text='Select Lesson:').grid(column=0,row=1,padx=10,pady=10)
ttk.Label(TAB6, text='Enter Plan:').grid(column=0,row=0,padx=10,pady=10)
PlanDet = StringVar()
lesson_plan = StringVar()
plan_lesson = ttk.Combobox(TAB6,textvariable=lesson_plan)
plan_lesson.grid(column=0,row=2,padx=10,pady=10)
Text(TAB6, width=50, height=20, wrap=WORD).grid(column=1,row=0,padx=10,pady=10)
ttk.Button(TAB6, text='Enter Details',command=lambda: addplan()).grid(column=3,row=1,padx=10,pady=10)
ttk.Button(TAB6, text='Add File',command=addplanfile).grid(column=3,row=0,padx=10,pady=10)
try: #IMPROVE
    with open("lessons.p","rb") as lesson_file:
        data1 = pkl.load(lesson_file)
except:
    data1 = []
displaydata1 = []
#try:
for item in data1:
    displaydata1.append(item.Location)
#print(type(plan_lesson))
plan_lesson['values'] = displaydata1
plan_lesson.grid(column=1,row=1,padx=10,pady=10) 
plan_lesson.current()
#except TypeError:
#    pass

#TAB7 Contents - Add Lesson Details
ttk.Label(TAB7, text='Add Location:').grid(column=0,row=0,padx=10,pady=10)
LocationID=StringVar()
ttk.Label(TAB7, text='Add Class:').grid(column=0,row=1,padx=10,pady=10)
AcaClassID=StringVar()
ttk.Label(TAB7, text='Add Subject:').grid(column=0,row=2,padx=10,pady=10)
SubjectID=StringVar()
ttk.Label(TAB7, text='Add Teacher:').grid(column=0,row=3,padx=10,pady=10)
TeacherID=StringVar()
ttk.Label(TAB7, text='Add Period:').grid(column=0,row=4,padx=10,pady=10)
PeriodID=StringVar()
ttk.Label(TAB7, text='Add Plan:').grid(column=0,row=5,padx=10,pady=10)
PlanID=StringVar()

ttk.Entry(TAB7, textvariable=LocationID).grid(column=1,row=0,padx=10,pady=10)
ttk.Entry(TAB7, textvariable=AcaClassID).grid(column=1,row=1,padx=10,pady=10)
ttk.Entry(TAB7, textvariable=SubjectID).grid(column=1,row=2,padx=10,pady=10)
ttk.Entry(TAB7, textvariable=TeacherID).grid(column=1,row=3,padx=10,pady=10)
ttk.Entry(TAB7, textvariable=PeriodID).grid(column=1,row=4,padx=10,pady=10)
ttk.Entry(TAB7, textvariable=PlanID).grid(column=1,row=5,padx=10,pady=10)
ttk.Button(TAB7, text='Enter Details',command=lambda: addlesson()).grid(column=2,row=0,padx=10,pady=10)

#TAB10 Contents - View Time Table

# Extracting data from selection
def selectItem(a):
    try:
        fh = open('plans.p','rb')
        plan_list = pkl.load(fh)
        fh.close()
    except FileNotFoundError:
        pass
    selected = TimeTable.focus() #Record Number
    # record values
    values = TimeTable.item(selected, 'values')
    print (values[1])
    LinearSearch(plan_list,values[1])


TimeTable = ttk.Treeview(TAB10)

# Defining Columns
TimeTable['columns'] = ("LessonID","Period","Subject","Class","Location")

#Format Columns
TimeTable.column("#0", width=0, stretch=NO)
TimeTable.column("LessonID", anchor=W, width=120)
TimeTable.column("Period", anchor=CENTER, width=120)
TimeTable.column("Subject", anchor=W, width=120)
TimeTable.column("Class", anchor=W, width=120)
TimeTable.column("Location", anchor=CENTER, width=120)

# Creat Headings
TimeTable.heading("#0", text="")
TimeTable.heading("LessonID", text="ID", anchor=W)
TimeTable.heading("Period", text="Period", anchor=W)
TimeTable.heading("Subject", text="Subject", anchor=W)
TimeTable.heading("Class", text="Class", anchor=W)
TimeTable.heading("Location", text="Location", anchor=W)

# Add Data
try:
    fh = open('lessons.p','rb')
    lessons_list = pkl.load(fh)
    fh.close()
except FileNotFoundError:
    pass

count = 0
for record in lessons_list:
    tt = record.timeTable()
    TimeTable.insert(parent='', index='end', iid=count, text="", values=(tt[4],tt[0],tt[1],tt[2],tt[3]))
    count += 1

#Assigning button press to extract data
TimeTable.bind('<ButtonRelease-1>', selectItem)
TimeTable.pack(pady=20)


mainWin.mainloop()
