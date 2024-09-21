class product:

    Pastry = 80
    CreamRoll = 70
    ChickenPetty = 50
    CakeRusk = 25
    FrenchFries = 100

def main():


    print("The prices of the products are:")
    print("Pastry = 80, Cream Roll = 70, Chicken Petty = 50, Cake Rusk = 25, French Fries = 100")
    print()

    khana = int(input("Enter the price of the product to order it: "))


    if khana == product.Pastry:
        print()
        print("You ordered Pastry")


    elif khana == product.CreamRoll:
        print()
        print("You ordered Cream Roll")


    elif khana == product.ChickenPetty:
        print()
        print("You ordered Chicken Petty")


    elif khana == product.CakeRusk:
        print()
        print("You ordered Cake Rusk")


    elif khana == product.FrenchFries:
        print()
        print("You ordered French Fries")



main()
