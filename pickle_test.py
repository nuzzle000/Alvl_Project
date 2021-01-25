import pickle
subjects = []
fh = open("subjects.p","rb")
subjects = pickle.load(fh)
print(subjects)