def check_list(l):
    count = 0
    for i in range(len(l)-1):
        if l[i] <= l[i+1]:
            count += 1
    if count == len(l)-1: return False
    return True
def main():
    print(check_list([1,2,3,4,5]))
main()