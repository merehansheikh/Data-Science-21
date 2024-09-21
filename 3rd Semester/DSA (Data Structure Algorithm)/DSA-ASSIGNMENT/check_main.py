from void_replace import *
from post_fix import *

# printing the list
def print_list(lst):
    for i in range(len(lst)):
        for j in range(len(lst[0])):
            print(lst[i][j], end="\t")
        print()

if __name__ == '__main__':
    # lst = [
    #     [1, 1, 1, 1, 1, 2, 1, 1, 2],
    #     [2, 2, 8, 2, 2, 2, 2, 1, 1],
    #     [2, 8, 8, 2, 2, 5, 7, 8, 2],
    #     [2, 8, 8, 2, 9, 2, 2, 8, 3],
    #     [4, 4, 0, 2, 9, 2, 6, 2, 2],
    #     [0, 4, 2, 2, 9, 2, 2, 2, 5],
    #     [9, 4, 2, 2, 2, 2, 2, 2, 4],
    #     [0, 4, 4, 4, 4, 4, 5, 4, 4]
    # ]
    # print_list(lst)
    # print("------------------------------------")
    # # (data, height, width, sr, sc, bc, fc)
    # void_replace(lst, 8, 9, 3, 5, 2, -1)
    # print_list(lst)


    # Checking the Post Fixed Impressions
    s = "123*+5+"
    print('The post fixed immression will be: ', end = '')
    print(post_fix(s))
    print("------------------------------------")
