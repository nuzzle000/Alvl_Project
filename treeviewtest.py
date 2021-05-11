from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Treeview - Test')
root.geometry("500x500")

my_tree = ttk.Treeview(root)

# Defining Columns
my_tree['columns'] = ("Name", "ID", "Favourite Colour")

# Format Columns
my_tree.column("#0", width=0, minwidth=0, stretch=NO)
my_tree.column("Name",anchor=W, width=120)
my_tree.column("ID",anchor=CENTER, width=80)
my_tree.column("Favourite Colour", anchor=W, width=120)

# Creat Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("Name", text="Name",anchor=W)
my_tree.heading("ID", text="ID", anchor=CENTER)
my_tree.heading("Favourite Colour", text="Favourite Colour", anchor=W)

# Add Data
data = [
    ["John", 1, "Blue"],
    ["Jack", 2, "Red"],
    ["James", 3, "Green"],
    ["Jasmine", 4, "Yellow"],
    ["Jerry", 5, "White"],
    ["Jade", 6, "Black"]
]


count=0
for record in data:
    my_tree.insert(parent='', index='end', iid=count, text="", values=(record[0],record[1],record[2]))
    count += 1



'''
my_tree.insert(parent='', index='end', iid=0, text="", values=("John",1, "Blue"))
my_tree.insert(parent='', index='end', iid=1, text="", values=("Jack",1, "Red"))
my_tree.insert(parent='', index='end', iid=2, text="", values=("James",1, "Green"))
my_tree.insert(parent='', index='end', iid=3, text="", values=("Jasmine",1, "Yellow"))
my_tree.insert(parent='', index='end', iid=4, text="", values=("Jerry",1, "White"))
my_tree.insert(parent='', index='end', iid=5, text="", values=("Jade",1, "Black"))
'''

# Add Child
#my_tree.insert(parent='0', index='end', iid=6, text="Child", values=("Steve", "1.2", "Cyan"))
#my_tree.move('6', '0', '0') Alternative to assign parent

# Pack to the screen
my_tree.pack(pady=20 )


root.mainloop()
