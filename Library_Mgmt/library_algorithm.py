from program import transaction
from program import return_transaction

def library():
    """The function where the user interacts with the library"""
    user_command = 0
    print("-------------------------------")
    print("Enter (1) to borrow books.")
    print("Enter (2) to return books.")
    print("Enter (3) to exit the program.")

    while user_command != 3:
        print("-------------------------------")
        while True:
            try:
                user_command = int(input("Enter your command: "))
                break
            except:
                print("Please enter a valid command.")
                print("-------------------------------")

        print("-------------------------------")
        if user_command == 1:
            transaction()
        elif user_command == 2:
            return_transaction()
        elif user_command == 3:
            print("Thank you for using this digital library program.")
            print()
            break
        else:
            print("Enter a valid command")


library()
