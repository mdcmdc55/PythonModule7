#!/usr/bin/python3

'''
requires python 3

use command line args: guest_list.py vendor_list.csv

program searches for a vendor name in the vendor csv and provides data associated with that vendor

option is given to update the vendor detail and save the changes to the vendor csv

'''

import csv
import sys

# function to determine which csv file to use
def findFile():
    fName = sys.argv[1]
    return fName

# call the function
fileName = findFile()

# open the file and use the csv.reader
vFile = open(r"C:\Users\stinkyshu\PycharmProjects\intro_to_python\{}".format(fileName), encoding="utf8")
csv_vf = csv.reader(vFile)

# skip the first row of headers
headersRow = next(csv_vf)
# i zipped the header row and data from each row to give a dict like {'vendor': 'Cisco', 'start_date' : '10/12/2017', 'end_date' : etc}
# but I couldn't figure out how to pull what I needed from it

# created menu to allow user to update the vendor data
def print_menu():
    print('\nEnter update option? ')
    print('1. vendor name')
    print('2. start date')
    print('3. end date')
    print('4. department')
    print('5. acct owner')
    print('6. save and exit')
    print()


vName = input("Enter Vendor Name: ")
field = 'vendor'
data = []
indx = headersRow.index(field)

# function to determine if Vendor is in current list
def whatvend(vName):
    for row in csv_vf:
        data.append(row[indx])
    try:
        if vName in data:
            pass
        else:
            addVendor = input("No vendor found. Add new vendor? ")
            if addVendor == "Y":
                newName = input('Vendor: ')
                newStart = input('Start Date: ')
                newEnd = input('End Date: ')
                newDept = input('Department: ').capitalize()
                newOwn = input('Acct Owner: ').title()
                newVend = [newName, newStart, newEnd, newDept, newOwn]
                # can't figure out how to write this new vendor info to the file!
                print("Vendor added.", newVend)
                x = newVend
    except:
        raise SystemExit("Invalid. System will exit.")

# have to re-open the file, need to figure out way to keep file open, I think using with open('file path here') as fileName
nFile = open(r"C:\Users\stinkyshu\PycharmProjects\intro_to_python\{}".format(fileName), encoding="utf8")
ncsv_f = csv.reader(nFile)

# function to pull existing vendor detail and make updates
def goVend(vName):
    for row in ncsv_f:
        if row[0] == vName:
            print('\nVendor: {}\n'
                  'Start Date: {}\n'
                  'End Date: {}\n'
                  'Department: {}\n'
                  'Account Owner: {}\n'.format(row[0],row[1],row[2],row[3],row[4]))
            rowVend = row
            updateVend = input("Press Enter to continue.")

            # setup counter to store menu choice
            menu_choice = 0
            # call function to display menu
            print_menu()
            # get menu choice from user
            while menu_choice != 6:
            # add error handler in case input is not a number
                try:
                    menu_choice = int(input("Type in a number (1-6): "))
                except ValueError:
                    print("\nYou must enter a number 1-6. Try again.\n")
                    print_menu()
                    continue

                # select what data to update
                if menu_choice == 1:
                    rowVend[0] = input('new name: ')
                    print_menu()

                elif menu_choice == 2:
                    rowVend[1] = input('new start: ')
                    print_menu()

                elif menu_choice == 3:
                    rowVend[2] = input('end date: ')
                    print_menu()

                elif menu_choice == 4:
                    rowVend[3] = input('dept: ')
                    print_menu()

                elif menu_choice == 5:
                    rowVend[4] = input('acct owner: ')
                    print_menu()

                else:
                    print("Changes made: ",rowVend)
                    # save the changes to the csv file!!
                    print("good-bye")

# call the functions
findFile()
whatvend(vName)
goVend(vName)



