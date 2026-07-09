patient={}

x1=input("Enter the Patient Name: ")

x2=int(input("Enter the age: "))

x3=int(input("Enter the Contact Number: "))

x4=input("Enter the Blood Group: ")

x5=input("Enter the Disease: ")

x6=input("Enter the Room Number: ")

print("Patient Record")

patient.update({"Name: ":x1})

patient.update({"Age: ":x2})

patient.update({"Contact Number: ":x3})

patient.update({"Blood Group: ":x4})

patient.update({"Disease: ":x5})

patient.update({"Room Number: ":x6})

print(patient)

# also write in this way
# patient["Name: "]=x1
# patient["Age: "]=x2
# print(patient)


