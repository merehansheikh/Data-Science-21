# [37, 90, 42, 84, 79, 97, 34, 31, 10, 59, 83, 64, 21, 74, 15, 56, 19, 46, 25, 13]
# [27, 80, 32, 74, 69, 87, 24, 21, 0, 49, 73, 54, 11, 64, 5, 46, 9, 36, 15, 3]

def minimum_value_in_list(l):
    small = l[0]
    for i in range(len(l)-1):
        if l[i] < small:
            small = l[i]

    return small

def main():

    d =[37, 90, 42, 84, 79, 97, 34, 31, 10, 59, 83, 64, 21, 74, 15, 56, 19, 46, 25, 13]

    print(minimum_value_in_list(d))
    print(list_minus_small(d, minimum_value_in_list(d)))
def list_minus_small(l, small):
    for i in range(len(l)):
        l[i] -= small
    return l
main()