student_list= []
student_quantity = int(input("How many students? "))

for i in range(student_quantity):
    student_name = input(f"Enter the name of student {i+1}: ")
    student_list.append(student_name)
print("\n")

search_name = input("Enter the Student to search: ")

def search_student(student_list, search_name):
    
    for student in student_list:
        if student == search_name:
            print("Student Found: ",student)
            break
    else:
        print("Student Not Found")

search_student(student_list, search_name)