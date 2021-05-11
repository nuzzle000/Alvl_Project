

data = []

def resetdata():
    global data
    data = []
    import random
    num = int(input("How many data items?"))
    data = []
    for i in range (0,num):   #create array with user length     
        x = random.randint(0,1000) #range of values
        data.append(x) #adding value(s) to array


#resetdata() #Running above code
data = [12,9,32,21,19,25,26]  ###HARDCODE DATA##

print("Current data:", data)

def LinearSearch():
    Found = False #Pointer for if data is found
    SearchItem = int(input("What do you want to find?"))

    for i in range (0, len(data)-1):
        if data[i] == SearchItem: #If data found then print found
            Found = True
            print("Found")

    if Found == False: # If data not found print not found
        print("Not Found")



def LinearSorted():
    BubbleSort() 
    Found = False
    SearchItem = int(input("What do you want to find?"))

    for i in range (0, len(data)-1):
        print(data[i])
        if data[i] == SearchItem:
            Found = True
            print("Found")
        elif data[i] > SearchItem:
            break

    if Found == False:
        print("Not Found")



def BinarySearch():
    BubbleSort()
    Start = 0
    Found = False
    End = int(len(data))-1
    SearchVal = int(input("Search: "))

    while Found == False and End >= Start:
        Middle = (Start + End)//2
        if data[Middle] == SearchVal:
            Found = True
            print ("Item found at position: ", Middle)
        elif SearchVal < data[Middle]:
            End = Middle - 1
        elif SearchVal > data[Middle]:
            Start = Middle + 1
        
    if Found == False:
        print ("Not Found")


def BinSrcRecursive():
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



def InsSort():
    for i in range (1, len(data)):
        ValtoSort = data[i]
        Ptr = i - 1
        while data[Ptr] > ValtoSort and Ptr > -1:
            data[Ptr + 1] = data[Ptr]
            Ptr = Ptr - 1
            print ("VAL",ValtoSort ,"moving", data, "PTR", Ptr)


        data[Ptr + 1] = ValtoSort
        print (i, data)


def sort(array=[12,4,5,6,7,3,1,15]):
    less = []
    equal = []
    greater = []
    

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
            print(array)
            print(pivot)
            sort(less)
            sort(equal)
            sort(greater)
            
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array
