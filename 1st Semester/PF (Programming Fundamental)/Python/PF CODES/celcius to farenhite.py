def cel_to_far(c):
    f = ((9/5)*(c) + 32)
    return f


def main():
    c = int(input("Enter the value of temperature in celcius: "))
    f = cel_to_far(c)
    print("The temperature in farenhite is:", round(f, 2))
main()

