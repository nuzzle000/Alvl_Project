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