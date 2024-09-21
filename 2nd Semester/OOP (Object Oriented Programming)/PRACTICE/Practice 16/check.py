def check_list(l):
    count = 0
    for i in range(len(l)-1):
        if l[i] <= l[i+1]:
            count += 1
    if count == len(l)-1: return False
    return True

def main():
    l = list(map(int, input().split()))
    count = 0
    i = 0
    while check_list(l):
            if l[i] == 1 and l[-1] == 0:
                l[-1] += 1
                count += 1
                i = 0
            elif l[i] == 1:
                l.append(1)
                l.pop(i)
                count += 1
                i = 0
            else:
                i += 1
    print(count)
    
main()