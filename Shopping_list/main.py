#proficiencyTest: Spotting list manager, Elisheva Kibbie 

# Make a list
shopping_list = []

# This is for adding stuff to the list
def add():
    item = input("Whadda ya want?(add): ")
    shopping_list.append(item)
    print(f"Stuffs added: {item}")
    print("Get Da stuffs:", shopping_list)

# This is for removing stuff from the list
def remove():
    item = input("I dont want it (remove): ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"stuffs thrown onto a random shelf: {item}")
    else:
        print(f"The thing: '{item}' dont got it. Didja speel its rite?")
    print("Stuffs i still gotta get:", shopping_list)

# Main loop that runs untill exit
while True:
    action = input("""polite buttler: What would you like young miss?
    Enter 1 to add item
    Enter 2 to remove item
    Enter 3 to leave the list:\n""")

    if action == "1":
        add()
    elif action == "2":
        remove()
    elif action == "3":
        print("dont let the door hit ya where the good lord split ya!")
        break
    else:
        print("FOR SHAME🙀, thats WRONG and out of bounds")
