menu ={
    "pizza": 5.00,
    "salad": 4.00,
    "cheese": 3.00,
    "fish": 7.00,
    "steak": 16.00
}


def run_restaurant():
    def take_order():
        def display_menu():
            for i in menu:
                print(i, ":", "$", menu[i])
        display_menu()

        def the_order():
            order = input("What would you like to order? ").lower()
            if order in menu:
                quantity = int(input("How many of these would you like? "))
                price = menu[order]*quantity
                print("Your total is: +$", price)
                any_else = str(input("Do you want anything else to order?yes/no "))
                if any_else == "yes":
                    display_menu()
                    the_order()
                    print("Your total is: +$", price)
                    '''
                    nuk ekziston full price te tregoje sa ke porositur total
                    '''
                elif any_else == "no":
                    print("Your order is", price)
            else:
                sorry = str(input("sorry, we dont have that, anything els ewe can help you with?yes/no"))
                if sorry == "yes":
                    display_menu()
                    the_order()
                elif sorry == "no":
                   print("Sorry we cannot help you, have a good day!")
        the_order()
    take_order()
run_restaurant()
