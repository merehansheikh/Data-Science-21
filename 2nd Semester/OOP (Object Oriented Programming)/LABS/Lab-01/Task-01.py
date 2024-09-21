import random

def main():
    count = 0
    less_than_fifty = 0
    for i in range(100):
        x = random.randint(0,100)
        count += 1
        if x < 50:
            less_than_fifty += 1
    print(count)
    print(less_than_fifty)
main()
