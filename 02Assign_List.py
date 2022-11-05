# Write a python program that do the following:

# - display the initial content of the array
# - display a menu of options
# - allow user to select item in the menu (check if valid)
# - perform the selected option (you may prompt additional info to user when need)
# - display the resulting values of the array


# Note: 
# - The program has an array variable containing 10 random numbers
# - You may add other options and features
# - Your program should be uploaded to github before 1:30pm
# - Record a demo presenting your program
# - Send the demo directly to my messenger

import random
totalvalues = 10
min = 0
max = 100
OFFSETT = 4
 
list= [48, 3, 10, 22, 35, 40, 99, 56, 69, 77]


# Main Menu

def get_list_values():
    return sorted(random.sample(range(min, max), totalvalues)) 

def list_menu():
    print(' \n \n')
    print("                                                Welcome Aboard Player!")
    options = ["Reverse Elements", "Sort the Elements", "Delete an Element","Add an Element", "Sort in  Decending order", "Sum of all Elements", "Exit Program" ]
    
    print("                              Your Array is this:",list, "\n")
    print(' \n \n')
    print("What would you like to do ?")
    for i, opt in enumerate(options):
        print(i+1, opt)
    


# Sum of all Elements        
def sum_element():
    sumlist = sum(list)
    print("\nThe sum of the values in the list is: ", sumlist, "\n")
    print("\nYour New Array: ", list, "\n")
    main()
    
def desc_element():
    list.sort()
    list.reverse()
    print("The list has been arranged in descending order!")
    print("\nYour New Array: ", list, "\n")
    main()
    
# Reverse Elements   
def rev_element():
    list.reverse()
    print("The list has been reversed!")
    print("\nYour New Array: ", list, "\n")
    main()
    
# Sort Elements
def sort_element():
    list.sort()
    print("\nYour New Array: ", list, "\n")
    main()
    
# delete element
def delete_element():
    while len(list) >= totalvalues:
        pickdel = input("Select the number you want to delete from the list: ")
        try:
            pickdel = int(pickdel) 
        except:
            print("Error! Your input must be an integer.")
            continue
        if pickdel in list:
            list.remove(pickdel)
            print("The number has been deleted!")
            print("\nYour New Array: ", list, "\n")
            main()
        else:
            print("Error! Your number was not in the list!")

def add_element():
    while len(list) >= totalvalues:
        add = input("Input the number between {} and {} that you want to add to this list: ".format(min, max))
        try:
            add = int(add)
        except:
            print("Error! Your input must be an integer.")
            continue
        if min <= add <= max:
            list.append(add)
            print("The number has been added!")
            print("\nYour New Array: ", list, "\n")
            main()
        else:
            print("Error! Your number was not in range")

            
def main():
    list_menu()
    while True:
        choice = input("\nEnter your choice[1-5]: ")
        if choice == '1':
            rev_element()
            break
        elif choice=='2' :
            sort_element()
            break
        elif choice== '3':
            string = '\n'"Delete an element " + "selected!"
            print(string)
            delete_element()
            break   
        elif choice=='4':
            string = '\n'"Add an element " + "selected!"
            print(string)
            add_element()
            break   
        elif choice == '5':
            string = '\n'"Arrange in descending order " + "selected!"
            desc_element()            
            break
        elif choice == '6':
            string = '\n'"Find the sum " + "selected!"
            sum_element()
            break
        elif choice== '7':
            print ("Thank You for Playing!\n")
            break
        else:
            print("Invalid option.")
            
main()

