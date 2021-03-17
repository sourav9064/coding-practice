##FULLY AUTOMATIC VENDING MACHINE – dispenses your cuppa on just press of button. A vending machine can serve range of products as follows:
##
##Coffee
##
##Espresso Coffee
##Cappuccino Coffee
##Latte Coffee
##Tea
##
##Plain Tea
##Assam Tea
##Ginger Tea
##Cardamom Tea
##Masala Tea
##Lemon Tea
##Green Tea
##Organic Darjeeling Tea
##Soups 
##
##Hot and Sour Soup
##Veg Corn Soup
##Tomato Soup
##Spicy Tomato Soup
##Beverages
##
##Hot Chocolate Drink
##Badam Drink
##Badam-Pista Drink
##Write a program to take input for main menu & sub menu and display the name of sub menu selected in the following format (enter the first letter to select main menu):
##
##Welcome to CCD 
##
##Enjoy your
##
##Example 1:
##
##Input:
##c
##1
##Output
##Welcome to CCD!
##Enjoy your Espresso Coffee!
##Example 2:
##
##Input
##t
##9
##Output
##INVALID OUTPUT!







menu = [["Espresso Coffee","Cappuccino Coffee","Latte Coffee"],
        ["Plain Tea","Assam Tea","Ginger Tea","Cardamom Tea","Masala Tea","Lemon Tea","Green Tea","Organic Darjeeling Tea"],
        ["Hot and Sour Soup","Veg Corn Soup","Tomato Soup","Spicy Tomato Soup"],
        ["Hot Chocolate Drink","Badam Drink","Badam-Pista Drink"]]

m = input()

if m=="c" or m=="t" or m=="s" or m=="b":
    if m=="c":
        sub = int(input())
        if sub in range(3):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[0][sub-1]))
        else:
            print("INVALID OUTPUT!")
    if m=="t":
        sub = int(input())
        if sub in range(8):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[1][sub-1]))
        else:
            print("INVALID OUTPUT!")
    if m=="s":
        sub = int(input())
        if sub in range(4):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[2][sub-1]))
        else:
            print("INVALID OUTPUT!")
    if m=="b":
        sub = int(input())
        if sub in range(3):
            print("Welcome to CCD!\nEnjoy your {}!".format(menu[3][sub-1]))
        else:
            print("INVALID OUTPUT!")
else:
    print("INVALID OUTPUT!")
        












