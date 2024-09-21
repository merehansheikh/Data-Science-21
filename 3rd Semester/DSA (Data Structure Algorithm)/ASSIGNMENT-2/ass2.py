from LinkedStack import *
from CityData import *


def open_file():
    # file_name = 'pb.txt'
    file_name = input('Enter File Name Storing A Network: ')

    fo = open(file_name, 'r')
    length_of_file = fo.readline().rstrip(' ')
    lst_of_city_data = []
    
    # putting the data(classes/ojects) in the list
    for _ in range(int(length_of_file)):
        lst = []
        data = fo.readline().rstrip('\n').split(' ')
        index = int(data[0])
        name = data[1].rstrip(',')
        count = int(data[2])
        for i in range(3, len(data)):
            lst.append(int(data[i]))
    
        ct_dt = CityData(index, name, count, lst)
        lst_of_city_data.append(ct_dt)
        # ====================
        print_fazool_data(lst_of_city_data)

    return lst_of_city_data


def search_city(lst):
    stk = LinkedStack()

    # finding the starting city and checcking whether it exist in the list or not
    st_ct = input('Enter the name of starting city: ')
    flag = True
    while flag:
        for i in range(len(lst)):
            if lst[i].name == st_ct:
                flag = False
                stk.push(i)
                break
        if not flag:
            break
        st_ct = input("Enter Valid Starting City Name >HEHE< : ")

    # finding the destination and checking
    dt_ct = input('Enter the name of Destination City: ')
    flag = True
    while flag:
        for i in range(len(lst)):
            if lst[i].name == dt_ct:
                flag = False
                break
        if not flag:
            break
        dt_ct = input("Enter Valid Destination City Name >< : ")

    while stk.isEmpty() != True:
        cc = stk.pop()

        if lst[cc].name == dt_ct:
            print("JOB DONE! PATH IS FOUND")
            path = [lst[cc].name]
            while lst[cc].predecessor != -1:
                cc = lst[cc].predecessor
                path.append(lst[cc].name)

            print_path(path)
            # =================================
            print_fazool_data(path)
            return

        else:
            oc = lst[cc].outCons
            for i in range(len(oc)):

                if lst[oc[i]].seen == False:
                    lst[oc[i]].set_seen()
                    lst[oc[i]].set_predecessor(cc)
                    stk.push(oc[i])

    if stk.isEmpty():
        print("Path Not found, LOL")

def print_fazool_data(path):
    print(path)


def print_path(path):
    s = ''
    for i in range(len(path)-1, -1, -1):
        if i == 0:
            s += path[i]
        else:
            s += path[i] + ' ---> '
    print(s)


def main():
    lst_of_ct = open_file()
    search_city(lst_of_ct)


if __name__ == '__main__':
    main()
