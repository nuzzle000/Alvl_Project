import pickle
with open("subjects.p","rb") as subject_file:
    data = pickle.load(subject_file)
for i in range (len(data)):    
    print(data[i].name)