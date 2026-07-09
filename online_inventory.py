inventory = {
    "Mouse":30,
    "Keyboard":45,
    "Monitor":25,
    "HDMI":100,
    "SSD":19
}
print("The Inventory Items are: ",inventory)

# update the items
inventory["Mouse"] = 50
print("Inventory items after update: ",inventory)

# add the item
inventory["Wireless Mouse"] = 40
print("Inventory items after adding the items: ",inventory)

# delete the item
del inventory["HDMI"]
print("Inventory items after delete: ",inventory)