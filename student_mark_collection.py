marks=[]

subjects = int(input("How many subjects: "))

for i in range(subjects):

    mark = int(input("Enter marks: "))

    marks.append(mark)
    
print("The marks are: ",marks)