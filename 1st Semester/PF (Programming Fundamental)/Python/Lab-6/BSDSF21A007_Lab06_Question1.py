class employ:
    ceo = "Soban"
    director = "Ali"
    manager = "Ahmed"
    clerk = "Sohaib"
    salesman = "Ahmer"
    receptionist = "Abdul Rahman"
    driver = "Abdullah"
    peon = "Azeem"


def main():


    desig = str(input("Enter your First name: "))

    if desig == employ.ceo:
        print("You are the CEO of the company")
    elif desig == employ.director:
        print("You are the Director of the company")
    elif desig == employ.manager:
        print("You are the Manager of the company")
    elif desig == employ.clerk:
        print("You are the Clerk of the company")
    elif desig == employ.salesman:
        print("You are the Salesman of the company")
    elif desig == employ.receptionist:
        print("You are the Receptionist of the company")
    elif desig == employ.driver:
        print("You are the Driver of the company")
    elif desig == employ.peon:
        print("You are the Peon of the company")

main()
