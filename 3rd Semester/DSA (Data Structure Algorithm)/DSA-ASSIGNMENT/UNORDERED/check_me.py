from unordered import *

            
def main():
    # Create a new Doubly Linked List
    AL = Unordered()
    # Insert the element to empty list
    AL.append(10)
    # Insert the element at the end
    AL.append(20)
    AL.append(30)
    AL.append(70)
    AL.append(50)
    AL.append(60)
    AL.append(80)
    AL.append(90)
    AL.append(40)
    # Display Data
    print("Display 10 items")
    AL.Display()
    # Delete elements from start
    AL.remove(0)
    # Display Data
    print("Display without (removed) first item")
    AL.Display()
    print()

    print("OUTPUT of 'for d in AL:'")
    for d in AL:
        print(d)
    print()

if __name__ == '__main__':
    main()