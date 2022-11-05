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
 
genlist= [1, 3, 10, 22, 35, 40, 47, 56, 69, 77]


# 'menu', creates the main menu to choose option or exit program

def get_list_values():
    return sorted(random.sample(range(min, max), totalvalues)) 

def list_menu():
    name = "Welcome Aboard Player"
    dotted = (OFFSETT+len(name))*''
    genlist = get_list_values()
    options = ["Reverse Elements", "Sort the Elements", "Delete an Element", "Sum of all Elements", "Exit Program" ]
    print('{} \n{} \n{}'.format(dotted, name, dotted))
    print("\nArray: ","[1, 3, 10, 22, 35, 40, 47, 56, 69, 77]", "\n")
    print("What would you like to do ?")
    for i, opt in enumerate(options):
        print(i+1, opt)
    print(dotted)


# Sum of all Elements        
def sum_element():
    sumlist = sum(genlist)
    print("\nThe sum of the values in the list is: ", sumlist, "\n")
    print("\033[01m\nYour New Array: ", genlist, "\n\033[01m")
    main()
    
def rev_element():
    genlist.reverse()
    print("The list has been reversed!")
    print("\033[01m\nYour New Array: ", genlist, "\n\033[01m")
    main()
    
# Sort Elements
def sort_element():
    genlist.sort()
    print("\033[01m\nYour New Array: ", genlist, "\n\033[01m")
    main()
    

# delete element
def delete_element():
    while len(genlist) >= totalvalues:
        pickdel = input("Select the number you want to delete from the list: ")
        try:
            pickdel = int(pickdel) 
        except:
            print("Sorry! Your input must be an integer.")
            continue
        if pickdel in genlist:
            genlist.remove(pickdel)
            print("\033[01m'The number has been deleted!'\033[01m")
            print("\033[01m'\nYour New Array: ", genlist, "\033[01m\n")
            main()
        else:
            print("Error! Your number was not in the list!")

            
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
        elif choice == '4':
            string = '\n'"Find the sum " + "selected!"
            sum_element()
            break
        elif choice== '5':
            print ("Thank You for Playing!\n")
            break
            
main()

