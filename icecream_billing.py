#!/usr/bin/env python
"""
# This code is to facilitate and automate Ice cream shop
# Date/Time: 28-May-2021 1:40pm
# Author: Vudayagiri Nagaraju
# Contact: vudayagiri.nagaraju@ltts.com
"""
# Ice cream and flavours list
icecream_list = {"Cup": 25, "Cone": 30, "Scoop": 50, "Box": 200}
flavour_list = {"Vennala": 5, "Butterscotch": 10, "Chocolate": 15}
DEALER_PWD = "Hello@123"
ADMIN_PWD = "Welcome@123"
COUPON_DISC = 50
ADM_VAL = 0


def icecream_update(name, flavour_name):
    """This function is to update a new ice cream/flavour and its price into the list """
    while True:
        try:
            price = int(input("Enter the ice cream price: "))
            break
        except ValueError:
            print("Invalid ice cream price")
    if name not in icecream_list.keys():
        while True:
            try:
                flavour_price = input("Enter the " + flavour_name + "flavour price: ")
                break
            except ValueError:
                print("Invalid flavour price")

        if flavour_name not in flavour_list.keys():
            icecream_list[name] = price
            flavour_list[flavour_name] = int(flavour_price)
            print("New ice cream and flavour added successfully")
            return 1
        icecream_list[name] = price
        flavour_list[flavour_name] = int(flavour_price)
        print("Ice cream prices updated successfully")
        return 1
    print("\nIce cream already exists")
    return 0


def icecream_add(name):
    """This function is to add/update a new ice cream/flavour and its price into the list """
    while True:
        try:
            price = int(input("Enter the ice cream price: "))
            break
        except ValueError:
            print("Invalid ice cream price")
            
    if icecream_search(name):
        print("\nIce cream already exists")
    else:
        icecream_list[name] = price
        print("Ice cream added successfully")
    return 0


def flavour_add(flavour_name):
    """This function is to add/update a new ice cream/flavour and its price into the list """
    while True:
        try:
            flavour_price = input("Enter the " + flavour_name + "flavour price: ")
            break
        except ValueError:
            print("Invalid flavour price")

    if flavour_search(flavour_name):
        print("\nFlavour already exists")
    else:
        flavour_list[flavour_name] = int(flavour_price)
        print("New flavour added successfully")
    return 0


def icecream_view():
    """This function is to view the list of available ice creams"""
    print("Ice creams available now")
    cnt = 1
    for i in icecream_list.keys():
        print("{} Ice Cream: {:<10} Price: Rs. {}".format(cnt, i, icecream_list[i]))
        cnt = cnt + 1

    for j in flavour_list.keys():
        print("{:<15} extra price: Rs. {}".format(j, flavour_list[j]))
    return 1


def icecream_search(name):
    """This function is used to search a ice cream """
    if name in icecream_list.keys():
        return 1
    else:
        return 0


def flavour_search(flavour_name):
    """This function is used to search a ice cream flavour """
    if flavour_name in flavour_list.keys():
        return 1
    else:
        return 0


def ice_flavour_search(name, flavour_name):
    """This function is used to search a ice cream by its flavour"""
    name_flag = icecream_search(name)
    flavour_flag = flavour_search(flavour_name)
    if name_flag:
        print(" Ice cream " + name + " is available in ")
    else:
        print(" Ice cream " + name + " is NOT available in ")

    if flavour_flag:
        print(" flavour " + flavour_name)
    else:
        print(" flavour " + flavour_name + "  Out of stock\n")

    if name_flag and flavour_flag:
        return 1
    else:
        return 0


def calculate_cost(icecream, flavour_name, total_quantity):
    price = icecream_list[icecream]
    flavour_price = flavour_list[flavour_name]
    cost = (flavour_price + price) * total_quantity
    return cost


def order_icecream(coupon_disc=0):
    """This function is to get customer input and order ice creams accordingly"""
    customer_name = input("Enter customer name: ")
    total_amount = 0.0
    total_orders = 0
    while True:
        total_quantity = 0
        while True:
            # get the ice cream from customer
            icecream = input("Choose the Ice cream you wish to enjoy: ")
            if icecream_search(icecream) is False:
                print("Invalid Ice cream")
                break

            # get the flavour from customer
            flavour_name = input("Choose the Flavour: ")
            if flavour_search(flavour_name) is False:
                print("Invalid Ice cream")
                break

            # get the quantity from customer
            try:
                total_quantity = 0
                total_quantity = int(input("Enter the total quantity: "))
                break
            except ValueError:
                print("Invalid quantity")
            break

        # calculate the cost of item
        if icecream_search(icecream):
            if flavour_search(flavour_name):
                item_cost = calculate_cost(icecream, flavour_name, total_quantity)
                total_amount += item_cost

        # writing order data in to the file data.txt
        with open("data.txt", "a") as dat:
            dat.write("Item No: " + str(total_orders + 1) + "\t")
            dat.write(" " + flavour_name + "\t")
            dat.write(" " + icecream + " ice cream ordered " + "\t")
            dat.write(" " + str(total_quantity) + " quantity." + "\t")
            dat.write(" Cost is Rs. " + str(item_cost) + "\n")
            dat.close()

        # If want to order more items.
        next_order = int(input("\nEnter 1 to order more. Else 2 to check out: "))
        if next_order == 2:
            print("Ice cream ordered successfully!")
            break
        elif next_order == 1:
            total_orders += 1
            continue
        else:
            print("\n Invalid Input")

    # print total bill based on coupon discount
    print("Customer Name: Mr/Mrs. " + customer_name + "\t")
    if coupon_disc and (total_amount > 200):
        print("Amount to be paid: ", total_amount - COUPON_DISC, " [Coupon Applied!] \n")
    else:
        print("Amount to be paid: ", total_amount, "\n")
    print("-----------------------------------------", + "\n")

    # writing total bill amount to the file data.txt
    with open("data.txt", "a") as dat:
        dat.write("Customer Name: Mr/Mrs. " + str(customer_name) + "\n")
        dat.write("Total Bill Amount : Rs. " + str(total_amount) + "\n")
        dat.write("-----------------------------------------\n\n")
        dat.close()
    print("Thank you for ordering. Enjoy the ice cream!! \n")
    input("Press any key for next customer.. ")
    return 0


def dealer_login(passwd):
    """To authenticate the dealer login"""
    if passwd == DEALER_PWD:
        return 1
    return 0


def admin_login(passwd):
    """To authenticate the admin login"""
    if passwd == ADMIN_PWD:
        return 1
    return 0


def view_orders():
    """To view the list of ice cream orders from the data file"""
    with open("data.txt", "r") as dat:
        print(dat.read())
        dat.close()
    return 1


def set_adm():
    """To set"""
    global ADM_VAL
    ADM_VAL = 1


def unset_adm():
    """To unset"""
    global ADM_VAL
    ADM_VAL = 0


def admin_menu():
    """Display as the Admin Home Screen"""
    while True:
        print("\n\nWelcome to the Ice Cream Shop\n")
        print("--------------------------------------", + "\n")
        print("Enter 1 to add an ice cream")
        print("Enter 2 to add a flavour")
        print("Enter 3 to view all ice creams")
        print("Enter 4 to check ice creams stock")
        print("Enter any other keys to exit: \n")
        while True:
            try:
                choice = int(input())
                break
            except ValueError:
                print("Invalid option")
        if choice == 1:
            name = input("Enter the ice cream you want to add: ")
            icecream_add(name)
        elif choice == 2:
            flv = input("Enter the ice cream flavour: ")
            icecream_add(flv)
        elif choice == 3:
            icecream_view()
        elif choice == 4:
            view_orders()
        else:
            break


def dealer_menu():
    """Display as the Dealer Home Screen"""
    while True:
        print("\n\nWelcome to the Ice Cream Shop\n")
        print("--------------------------------------\n")
        print("Enter 1 to view all ice creams")
        print("Enter 2 to search a ice cream")
        print("Enter 3 to order ice creams")
        print("Enter any other keys to exit\n")
        while True:
            try:
                choice = int(input())
                break
            except ValueError:
                print("Invalid option")
        if choice == 1:
            icecream_view()

        elif choice == 2:
            icecream = input("Enter the ice cream you want to search: ")
            flavour_name = input("Enter the flavour you want to search: ")
            ice_flavour_search(icecream, flavour_name)

        elif choice == 3:
            print("Want to order ice creams with or without coupon")
            opt = int(input("Enter 1 if No Coupon \nEnter 2 if Coupon"))
            if opt == 1:
                order_icecream()
            elif opt == 2:
                order_icecream(COUPON_DISC)
        else:
            break


def validate_user():
    print("\n\nWelcome to the Ice Cream Shop\n")
    print("--------------------------------------\n")
    passwd = input("Enter the password for admin/dealer login: ")
    if dealer_login(passwd):
        dealer_menu()
    elif admin_login(passwd):
        set_adm()
        admin_menu()
        unset_adm()
    else:
        print("Entered wrong password")


validate_user()
