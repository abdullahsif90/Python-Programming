print("Shopping List ")

with open("shopping_list.txt","a") as sl:
    list_entry = int(input("How many items you want to enter? "))
    for i in range(list_entry):
        item_entry = input(f"Enter the item no {i+1}: ")
        sl.write(item_entry + "\n")

# To read 
with open("shopping_list.txt","r") as sl:
    print("\n Updated List: ")
    print(sl.read())
print("All items saved successfully")
