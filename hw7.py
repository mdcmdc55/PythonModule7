#!/usr/bin/env python3
'''
working with sorted dictionary

requires: python3


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
print_menu()


# as long as the menu choice isn't "quit" get user options
while menu_choice != 5:
    # get menu choice from user
    # add error handler in case input is not a number
    try:
        menu_choice = int(input("Type in a number (1-5): "))
    except ValueError:
        print("\nYou must enter a number 1-5. Try again.\n")
        print_menu()
        continue

    # view current entries
    if menu_choice == 1:
        print("Current Users:\n")
        for x, y in usernames.items():
            print("Name: {} \tUser Name: {} \n".format(x, y))
        print_menu()

    # add an entry
    elif menu_choice == 2:
        print("Add User")
        name = input("Name: ")
        username = input("User Name: ")
        usernames[name] = username
        print("\nUser added.\n")
        print_menu()

    # remove an entry
    elif menu_choice == 3:
        print("Remove User")
        name = input("Name: ")
        # add while loop to give 3 attempts to enter valid user
        count = 0
        while name not in usernames and count < 3:
            print("Invalid entry. Try again.\n")
            name = input("Name: ")
            count += 1
            continue
        if name in usernames:
            del usernames[name]
            print("\nUser removed.\n")
            print_menu()
            ### pass  # delete that entry
        else:
            print("Invalid entry. Unable to complete the request.\n")
            print_menu()

    # view user name
    elif menu_choice == 4:
        print("Lookup User")
        name = input("Name: ")
        # add while loop to give 3 attempts to enter valid user
        count = 0
        while name not in usernames and count < 3:
            print("Invalid entry. Try again.\n")
            name = input("Name: ")
            count += 1
            continue
        if name in usernames:
            print("Username: ", usernames[name], "\n")
            print_menu()
        else:
            print("Invalid entry. Unable to complete the request.\n")
            print_menu()

    # if user enters a number other than 1-5
    elif menu_choice != 5:
        print("Not a valid menu choice. Try again.\n")
        print_menu()