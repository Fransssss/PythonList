# list = store multiple values

print("\nList - Store multiple values\n")
list = []
print("== List Menu ==")
print("1. List items ")
print("2. Add an item")
print("3. Add an item at specified position")
print("4. Sort the list")
print("5. Take out last item")
print("6. Remove an item")
print("7.  Clear the list")
print("E. Exit")
choice = input("choice: ")
print('\n')

while choice != "E" and choice != "e":
    if choice == "1":
        print("List item: ")
        print(list)
        print('\n')
    elif choice == "2":
        print("Add an item")
        add = input("Input an item to add: ")
        list.append(add)
        print('Item has been added\n')
    elif choice == "3":
        print("Add an item at specified position")
        ins = input("Input an itme to add: ")
        pos = int(input("input an index in the list: "))
        list.insert(pos,ins)
        print('Item has been added\n')
    elif choice == "4":
        print("Sort the list")
        list.sort()
        print(list)
        print('\n')
    elif choice == "5":
        print("Take out the last item")
        list.pop()
        print('Last Item has been taken out\n')
    elif choice == "6":
        print("Remove an item")
        remv = input("input the name of item to remove: ")
        list.remove(remv)
        print('Item has been removed\n')
    elif choice == "7":
        print("Clear the list")
        list.clear()
        print('List has been cleared\n')
    else:
        print("Invalid choice")

    print("== List Menu ==")
    print("1. List items ")
    print("2. Add an item")
    print("3. Add an item at specified position")
    print("4. Sort the list")
    print("5. Take out last item")
    print("6. Remove an item")
    print("7.  Clear the list")
    print("E. Exit")
    choice = input("choice: ")
    print('\n')


