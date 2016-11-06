
shopping_list = []

def add_items():
    print("Please add the desired items")
    print("Enter 'DONE' to exit, 'SHOW' to view items or 'HELP' to view this menu!")

    while True:
        item = input("> ")

        if item == 'DONE':
            break
        elif item == 'SHOW':
            print("The items in the list are: {}".format(", ".join(shopping_list)))
        elif item == 'HELP':
            print("Enter 'DONE' to exit, 'SHOW' to view items or 'HELP' to view this menu!")
        else:
            shopping_list.append(item)

add_items()

if len(shopping_list) > 0:
    print("Your list contains: {}".format(", ".join(shopping_list)))
else:
    print("There are no items in the list")

