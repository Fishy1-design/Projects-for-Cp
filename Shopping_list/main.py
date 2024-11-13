#proficiencyTest: Spotting list manager, Elisheva Kibbie 

# Create an empty shopping list
shopping_list = []

# Define function to add an item to the shopping list
def add():
    item = input("Whadda ya want?(add): ")
    shopping_list.append(item)
    print(f"Stuffs added: {item}")
    print("Get Da stuffs:", shopping_list)

# Define function to remove an item from the shopping list
def remove():
    item = input("I dont want it (remove): ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"stuffs thrown onto a random shelf: {item}")
    else:
        print(f"The thing: '{item}' dont got it. Didja speel its rite?")
    print("Stuffs i still gotta get:", shopping_list)

# Main loop that keeps the program running until the user decides to leave
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
