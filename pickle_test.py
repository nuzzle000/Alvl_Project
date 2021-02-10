import pickle
subjects = []
fh = open("subjects.p","rb")
subjects.append(pickle.load(fh))
print(subjects)