print("Student Marks Recorder")

with open("student_marks.txt","a") as sm:
    student =int(input("How many students you want to enter? "))
    for i in range (student):
        name = input(f"Enter the student name no {i+1}: ")
        marks =input(f"Enter the marks for student {i+1}: ")
        # sm.write(name + "\n")
        # sm.write(marks + "\n")
        sm.write(name + " - " + marks + "\n")

with open("student_marks.txt", "r") as sm:
    print("Updated List is: ")
    print(sm.read())