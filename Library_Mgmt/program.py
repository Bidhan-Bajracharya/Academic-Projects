import datetime
import random


def display_books():
    """Displays book's in stock"""
    stock_file = open("stockbooks.txt", "r")
    read_handle = stock_file.readlines()
    print("These are the books available for you to borrow: ")
    print()
    stock_file.close()
    display_data = []
    for info in read_handle:
        info = info.replace("$", "")
        display_data.append(info.replace("\n", "").split(","))

    for i in range(len(display_data)):
        print(f"Name: {display_data[i][0]}, Author: {display_data[i][1]}, Quantity: {display_data[i][2]}, Price: ${display_data[i][3]}")
    

def buy_bill(customer_name, customer_bought, customer_payment, id_):
    """Bill format when user borrows a book"""
    bill = open(id_ + "bill.txt", "w")
    bill.write(f"--------------THANK YOU-------------- \n")
    bill.write(f"Customer name: {customer_name}   \n")
    bill.write("-------------------------------------  \n")
    bill.close()

    # displaying all the books the user borrowed
    bill_append = open(id_ + "bill.txt", "a")
    for i in range(len(customer_bought)):
        bill_append.write(f"Book's borrowed: {customer_bought[i][0]}  \n")

    bill_append.write("-------------------------------------  \n")

    # displaying the quantity of books borrowed
    for j in range(len(customer_bought)):
        bill_append.write(f"{customer_bought[j][0]} : {customer_bought[j][1]} piece(s)  \n")

    bill_append.write("-------------------------------------  \n")
    bill_append.write(f"Your total payment: ${customer_payment}    \n")
    bill_append.write("-------------------------------------  \n")
    bill_append.write(f"Date of Issue: {datetime.date.today()}  \n")
    bill_append.write(f"Time of Issue: {datetime.datetime.now().time()} \n")
    bill_append.write(f"-------------Visit Again-------------")
    bill_append.close()


def book_return_late(customer_name, extra_day, returned_books, borrowed_duration, random_ids):
    """Bill format when user returns a book exceeding the 10-day limit"""
    extra_pay = 0
    return_bill = open(random_ids + "return.txt", "w")
    return_bill.write(f"*NOTICE* \n")
    return_bill.write(f"Since you borrowed the book for extra {extra_day} day(s). \n")
    return_bill.write(f"An extra fee should be paid which is: 1 day = $5  \n")
    return_bill.write("\n")

    # charging extra $5 for every extra day
    for i in range(extra_day):
        extra_pay = extra_pay + 5

    return_bill.write(f"------------Thank You------------ \n")
    return_bill.write(f"Client's Name: {customer_name} \n")
    return_bill.write(f"--------------------------------- \n")
    return_bill.close()

    return_bill_append = open(random_ids + "return.txt", "a")
    for j in range(len(returned_books)):
        return_bill_append.write(f"Book's returned: {returned_books[j]} \n")

    return_bill_append.write(f"---------------------------------\n")
    return_bill_append.write(f"Date of return: {datetime.date.today()} \n")
    return_bill_append.write(f"Time of return: {datetime.datetime.now().time()} \n")
    return_bill_append.write(f"Borrowed Time: {borrowed_duration} days\n")
    return_bill_append.write(f"Extra Charge: ${extra_pay}  \n")
    return_bill_append.write(f"-----------Visit Again-----------")
    return_bill_append.close()


def book_return_ontime(customer_name, returned_book, borrowed_duration, random_ids):
    """Bill format when user returns a book within the 10-day limit"""
    return_bill = open(random_ids + "return.txt", "w")
    return_bill.write(f"------------Thank You------------ \n")
    return_bill.write(f"Client's Name: {customer_name} \n")
    return_bill.write(f"--------------------------------- \n")
    return_bill.close()

    return_bill_append = open(random_ids + "return.txt", "a")
    for i in range(len(returned_book)):
        return_bill_append.write(f"Book's returned: {returned_book[i]} \n")

    return_bill_append.write(f"---------------------------------\n")
    return_bill_append.write(f"Date of return: {datetime.date.today()} \n")
    return_bill_append.write(f"Time of return: {datetime.datetime.now().time()} \n")
    return_bill_append.write(f"Borrowed Time: {borrowed_duration} days\n")
    return_bill_append.write(f"-----------Visit Again-----------")
    return_bill_append.close()


def transaction():
    """Function for borrowing books"""
    random_id = str(int(random.random() * 100000))
    payment = 0
    user_ask = ""
    booking = open("stockbooks.txt", "r")
    transaction_handle = booking.readlines()
    booking.close()
    data = []
    book_names = []
    user_bought = []
    user_name = input("Enter your name: ")

    # removing the $ and \n from the price
    for price in transaction_handle:
        price = price.replace("$", "")
        data.append(price.replace("\n", "").split(","))

        # changing the quantity in int and prices in float format
        for i in range(len(data)):
            data[i][2] = int(data[i][2])
            data[i][3] = float(data[i][3])

    # storing names of all the books in a list
    for a in range(len(data)):
        book_names.append(data[a][0].lower())

    # continous loop unless the user wants to stop
    while user_ask.lower() != "n":
        user_ask = input("Do you wish to borrow books?[y/n]: ")
        print("---------------------------------------------")
        if user_ask.lower() == "y":
            display_books()
            print("---------------------------------------------")
            user_book_choice = input("Which book do u want to borrow?: ")
            if user_book_choice.lower() in book_names:
                while True:
                    try:
                        user_book_quantity = int(input("How many books do you want to borrow?: "))
                        if user_book_quantity <= 0:
                            print("Please enter a valid quantity")
                            print("-------------------------------")
                        else:
                            break
                    except:
                        print("Please enter a valid quantity.")
                        print("-------------------------------")

                for x in range(len(data)):
                    if data[x][0].lower() == user_book_choice.lower():
                        data[x][2] = data[x][2] - user_book_quantity
                        user_bought.append([data[x][0], user_book_quantity, data[x][3]])
                        payment = payment + (data[x][3] * user_book_quantity)
                        break

                # calling the bill module
                buy_bill(user_name, user_bought, payment, random_id)

            else:
                print("Please enter a valid book name.")
                print("-------------------------------")

        elif user_ask.lower() == "n":
            print("Thank you for visiting the store.")
            if len(user_bought) != 0:
                print(f"Please collect your bill with ID:{random_id}, after exiting the program.")
            print("-------------------------------")
            print("Enter (1) to borrow books.")
            print("Enter (2) to return books.")
            print("Enter (3) to exit the program.")

        else:
            print("Please enter a valid command.")
            print("-------------------------------")

    filing = open("stockbooks.txt", "w")
    filing.write(f"Harry Potter,JK Rowling,{data[0][2]},$2 \n")
    filing.write(f"Start With Why,Simon Sinek,{data[1][2]},$1.5 \n")
    filing.write(f"Programming With Python,John Smith,{data[2][2]},$1.5 \n")
    filing.write(f"Jane Eyre,John Smith,{data[3][2]},$1.5 \n")
    filing.write(f"The Alchemist,Paulo Coelho,{data[4][2]},$2 \n")
    filing.write(f"Animal Farm,George Orwell,{data[5][2]}, $1.5 \n")
    filing.write(f"The Beetle,Richard Marsh,{data[6][2]},$1.5 \n")
    filing.write(f"The Giver,Lois Lowry,{data[7][2]},$2")
    filing.close()


def return_transaction():
    """Function for returning books"""
    user_ask = ""
    user_name = input("Enter you name: ")
    books_return = []
    random_id = str(int(random.random() * 100000))
    booking = open("stockbooks.txt", "r")
    transaction_handle = booking.readlines()
    booking.close()
    stock_data = []
    returned_data = []
    book_names = []

    # removing the $ and \n from the price
    for price in transaction_handle:
        price = price.replace("$", "")
        stock_data.append(price.replace("\n", "").split(","))

        # inputting the quanitity in int and prices in float format
        for i in range(len(stock_data)):
            stock_data[i][2] = int(stock_data[i][2])
            stock_data[i][3] = float(stock_data[i][3])

    # storing all the names of the book in a list
    for a in range(len(stock_data)):
        book_names.append(stock_data[a][0].lower())

    # looping till user wants to stop
    while user_ask.lower() != "n":
        user_ask = input("Do you wish to return books?[y/n]: ")
        if user_ask.lower() == "y":
            borrowed_book = input("Which book are you trying to return?: ")
            print("-------------------------------")
            if borrowed_book.lower() in book_names:
                while True:
                    try:
                        borrowed_quantity = int(input("How many books?: "))
                        if borrowed_quantity <= 0:
                            print("Please enter a valid quantity")
                            print("-------------------------------")
                        else:
                            break
                    except:
                        print("Please enter a valid quantity.")
                        print("-------------------------------")

                books_return.append(borrowed_book)
                returned_data.append([borrowed_book.lower(), borrowed_quantity])
            else:
                print("Please enter a valid book name.")
                print("-------------------------------")

        elif user_ask.lower() == "n":
            break
        else:
            print("Please enter a valid command.")
            print("-------------------------------")

    while True:
        try:
            user_duration = int(input("How long have you had the book?(days): "))
            if user_duration <= 0:
                print("Please enter valid number of days.")
                print("-------------------------------")
            else:
                break
        except:
            print("Please enter valid number of days.")
            print("-------------------------------")

    # checking if the duration exceeds the 10 day limit
    if user_duration > 10:
        extra_days = user_duration - 10
        book_return_late(user_name, extra_days, books_return, user_duration, random_id)
        print(f"Please collect your bill with ID:{random_id}, after exiting the program.")
        print("-------------------------------")
        print("Enter (1) to borrow books.")
        print("Enter (2) to return books.")
        print("Enter (3) to exit the program.")
    else:
        book_return_ontime(user_name, books_return, user_duration, random_id)
        print(f"Please collect your bill with ID:{random_id}, after exiting the program.")
        print("-------------------------------")
        print("Enter (1) to borrow books.")
        print("Enter (2) to return books.")
        print("Enter (3) to exit the program.")

    # finding which book the user returned and updating the stock
    for i in range(len(returned_data)):
        for j in range(len(stock_data)):
            if returned_data[i][0] == stock_data[j][0].lower():
                if j == 0:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2] + returned_data[i][1]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[0][2] = stock_data[0][2] + returned_data[i][1]

                if j == 1:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2] + returned_data[i][1]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[1][2] = stock_data[1][2] + returned_data[i][1]

                if j == 2:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2] + returned_data[i][1]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[2][2] = stock_data[2][2] + returned_data[i][1]

                if j == 3:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2] + returned_data[i][1]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[3][2] = stock_data[3][2] + returned_data[i][1]

                if j == 4:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2] + returned_data[i][1]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[4][2] = stock_data[4][2] + returned_data[i][1]

                if j == 5:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2] + returned_data[i][1]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[5][2] = stock_data[5][2] + returned_data[i][1]

                if j == 6:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2] + returned_data[i][1]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2]},$2")
                    filing.close()
                    stock_data[6][2] = stock_data[6][2] + returned_data[i][1]

                if j == 7:
                    filing = open("stockbooks.txt", "w")
                    filing.write(f"Harry Potter,JK Rowling,{stock_data[0][2]},$2 \n")
                    filing.write(f"Start With Why,Simon Sinek,{stock_data[1][2]},$1.5 \n")
                    filing.write(f"Programming With Python,John Smith,{stock_data[2][2]},$1.5 \n")
                    filing.write(f"Jane Eyre,John Smith,{stock_data[3][2]},$1.5 \n")
                    filing.write(f"The Alchemist,Paulo Coelho,{stock_data[4][2]},$2 \n")
                    filing.write(f"Animal Farm,George Orwell,{stock_data[5][2]}, $1.5 \n")
                    filing.write(f"The Beetle,Richard Marsh,{stock_data[6][2]},$1.5 \n")
                    filing.write(f"The Giver,Lois Lowry,{stock_data[7][2] + returned_data[i][1]},$2")
                    filing.close()
                    stock_data[7][2] = stock_data[7][2] + returned_data[i][1]
                    
                    
