print("Student Marks Average System")

marks=[]
students=int(input("How many students? "))
for i in range(students):
    mark_entry=int(input(f"Enter mark of student {i+1}: "))
    marks.append(mark_entry)

def calculate_average(marks):
    total =0
    for mark in marks:
        total= total + mark
        average = total / len(marks)
    return average
    
average= calculate_average(marks)

if average >= 80:
    print("Excellent")
elif average >=60:
    print("Good")
else:
    print("Need Improvement")
