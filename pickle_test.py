import pickle as pkl
class Subject:
    def __init__(self,SubjectID,name,faculty,keystage):
        self.SubjectID = SubjectID
        self.name = name
        self.faculty = faculty
        self.keystage = keystage
    def printall(self):
        print(self.SubjectID, self.name, self.faculty, self.keystage)

fileObject = open('subjects.p','rb')
subject = pkl.load(fileObject)
fileObject.close()
subject.printall()
