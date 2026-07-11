print("Student Information System")

students = []

student = int(input("How many students? "))

for i in range(student):
    student_name = input(f"Enter the name of student {i+1}: ")
    student_age = int(input(f"Enter the age of student {i+1}: "))
    student_cgpa = float(input(f"Enter the CGPA of student {i+1}: "))

    student_data = {
        "Name": student_name,
        "Age": student_age,
        "CGPA": student_cgpa
    }

    students.append(student_data)

print("\nStudent Records")

for data in students:
    print(data)