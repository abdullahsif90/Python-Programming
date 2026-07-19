print("Feedback System")
print("Rate our app")

with open("feedback.txt","a") as feedback_file:
    feedback = int(input("How many feedback you want to enter? "))
    for i in range(feedback):
        feedback_entry= input(f"Enter the feedback no {i+1}: ")
        feedback_file.write(feedback_entry +"\n")

with open("feedback.txt","r") as  ff:
    print("Updated Feedback List is: ")
    print(ff.read())
    