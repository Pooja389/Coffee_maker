from data import MENU,resources
def get_money():
    # getting money from coustomer in INR
    ten = int(input("how many 10 rs note :"))
    fifty = int(input("how many 50 rs note :"))
    hundred = int(input("how manu 100 rs note :"))
    total_money = int(ten*10 + fifty*50 + hundred*100)
    return total_money

resources_are_left = True

# loop continues till resources meet the amount of resources needed to make ordered coffee
while resources_are_left:
    # asking the user to choose a coffee
    ask = int(input("\nwhat would you like to have espresso(100 Rs), latte(150 Rs) ,cappuccino(170 Rs)\ntype '1' for espresso, '2' for latte, '3' for cappuccino :"))
    
    if ask == "report":
        print(resources)

    if ask == 1:
        cost = MENU["espresso"]["cost"]
        coffee = "espresso"

    elif ask == 2:
        cost = MENU["latte"]["cost"] 
        coffee = "latte"

    elif ask == 3:
        cost = MENU["cappuccino"]["cost"]
        coffee = "cappuccino"

    else:
        print("provide a valid input")  
    # getting resources needed to make desired coffee
    required_water = MENU[coffee]["ingredients"]["water"]
    required_milk = MENU[coffee]["ingredients"]["milk"]
    required_coffee = MENU[coffee]["ingredients"]["coffee"]   
    
    # checking if resources are enough to make desired coffee
    if resources["coffee"] >= required_coffee  and resources["water"] >= required_water and resources["milk"] > required_milk:

        # getting hold of money given by caustomer
        money = get_money()
        change = money - cost  

        if money > cost:
            print("here is your change",change)
            print(f"here is your {coffee} enjoy")
        elif money < cost:
            print("you did not provide enough money")
        else:
            print(f"here is your {coffee} enjoy")    


        required_water = MENU[coffee]["ingredients"]["water"]
        required_milk = MENU[coffee]["ingredients"]["milk"]
        required_coffee = MENU[coffee]["ingredients"]["coffee"]

        # updating the resources in data
        resources["water"] -=  required_water
        resources["milk"] -=  required_milk
        resources["coffee"] -=  required_coffee
        
    else:
        # here the resources are not enough to make desired coffee so telling the user what resources are left
        print(f"resources are not enough to make {coffee}")
        print("resources left are\n",resources)
        

