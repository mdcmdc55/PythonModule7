#!/usr/bin/env python3
'''
requires: python3
add more detail to the docstring

'''

from sortedcontainers import SortedDict

def print_menu():
    print('1. Print Users')
    print('2. Add a User')
    print('3. Remove a User')
    print('4. Lookup a Username')
    print('5. Quit')
    print()

# Create dictionary with key = Names, value = user_name
usernames = SortedDict()
usernames['Summer'] = 'summerela'
usernames['William'] = 'GoofyFish'
usernames['Steven'] = 'LoLCat'
usernames['Zara'] = 'zanyZara'
usernames['Renato'] = 'songDude'

# setup counter to store menu choice
menu_choice = 0

# display your menu
##print_menu()

## add error handler in case input is not a number
# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    print_menu()
    menu_choice = int(input("Type in a number (1-5): "))
    # add error handling if input is not number
    # view current entries
    if menu_choice == 1:
        print("Current Users:")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
        ##ask teacher: how is the above working to append to the dict? - it's just appending without "append"
        # print(key, value)
        print(name, username, "has been added.\n")

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        # if name not found, allow 3 more attempts to enter a valid name
        count = 0
        while name not in usernames and count < 3:
            print("Invalid name. Try again.\n")
            #print("Enter name.")
            name = input("Name: ")
            count += 1
            continue
        if name in usernames:
            del usernames[name]
            print("{} has been removed.\n".format(name))
        else:
            print("Invalid name. Unable to complete the request.\n")

    # view user name
    elif menu_choice == 4:
        print("Lookup Username")
        name = input("Name: ")
        # same error handling as above
        count = 0
        while name not in usernames and count < 3:
            print("Invalid name. Try again.\n")
            #print("Enter a valid name.")
            name = input("Name: ")
            count += 1
            continue
        if name in usernames:
            print("Username is {}.\n".format(usernames[name]))
        else:
            print("Invalid name. Unable to complete the request.\n")

    # if user enters something strange, show them the menu
    # if user enters a number other than 1-5
    elif menu_choice != 5:
        print("Invalid entry.\n")
        continue
        #print_menu()