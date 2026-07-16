print("Personal Diary")

with open("diary.txt","a") as file:
    entry =input("Write today's diary: ")
    file.write(entry + "\n")
print("Diary entry saved successfully!")