
def decision1():
    import time
    print("welcome to Ficksburg Food Court, where we deliver anywhere and anytime between 7am-5pm Monday-Saturday for R25. Choose your actions\n1.Order\n2.Ask for assistance\n3.Delivery status\n4.Payment\n5.Exit ")

    customer1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (customer1.upper() == "1"):
            print("Where would you like to eat\n1.Wimpy\n2.Imperani\n3.KFC\n4.Wild BBQ")
            ans = 'correct'
            decision2()
        elif (customer1.upper() == "2"):
            print("We will connect you to our customer service soon, please wait a bit.")
            ans = 'correct'
        elif (customer1.upper() == "3"):
            print("The driver will contact you to send your delivery status soon")
            ans = 'correct'
        elif (customer1.upper() == "4"):
            print("We accept cash only.")
            ans = 'correct'
        elif (customer1.upper() == "5"):
            print("Thank you for using Ficksburg Food Court.Bye.")
            ans = 'correct'
        else:
            print("Sorry we do not understand")
            customer1 = input()


def decision2():
    import time

    customer1 = input()
    time.sleep(2)
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if (customer1.upper() == "1"):
            print("Would you like a menu?\n1.Yes\n2.No")
            customer1 = input()
            if (c1.upper() == "1"):
                print("https://food-menu-6924.twil.io/Breakfast_Griills_.pdf")
                print("Enter your order: ")
                ans = 'correct'
                decision3()
            elif (customer1.upper() == "2"):
                print("Alright, you may enter your order.")
                ans = 'correct'
                decision3()
        elif (customer1.upper() == "2"):
            print("Would you like a menu?\n1.Yes\n2.No")
            customer1 = input()
            if (customer1.upper() == "1"):
                print("https://food-menu-6924.twil.io/Imperani%20menu.pdf")
                ans = 'correct'
                decisoin3()
            elif (customer1.upper() == "2"):
                print("Alright, you may enter your order.")
                ans = 'correct'
                decision3()
        elif (customer1.upper() == "3"):
            print("Would you like a menu?\n1.Yes\n2.No")
            customer1 = input()
            if (customer1.upper() == "1"):
                print("https://food-menu-6924.twil.io/KFC.pdf")
                ans = 'correct'
                decision3()
            elif (customer1.upper() == "2"):
                print("Alright, you may enter your order.")
                ans = 'correct'
                decision3()
        elif (customer1.upper() == "4"):
            print("Would you like a menu?\n1.Yes\n2.No")
            customer1 = input()
            if (customer1.upper() == "1"):
                print("https://food-menu-6924.twil.io/BBq.jpg")
                ans = 'correct'
                decision3()
            elif (customer1.upper() == "2"):
                print("Alright, you may enter your order.")
                ans = 'correct'
                decision3()

        else:
            print("Sorry we do not understand")
            customer1 = input()


def decision3():
    import time
    time.sleep(2)
    customer1 = input()
    ans = 'incorrect'
    while (ans == 'incorrect'):
        if len(customer1.upper()) >= 1:
            print("Thank you, we will process your order")
            ans = 'correct'
        else:
            print("Sorry we do not understand")
            customer1 = input()
    time.sleep(2)




decision1()







