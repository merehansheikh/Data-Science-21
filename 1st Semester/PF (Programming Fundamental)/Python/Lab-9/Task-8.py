def append(ad, nd):
    for i in range(len(ad)):
        if ad[i] == -1:
            j = i
            break
    i = 0
    while j < len(ad):
        if nd[i] == -1:
            ad[i] = -1
            return ad
        ad[j] = nd[i]
        j += 1
        i+=1
        ad[j] = -1
    return ad


def main():
    ad = [3, 43, 69, 75, 32, 45, -1, 43, 68, 21, 23, 65, 98]
    nd = [21, 43, 98, -1, 89, 22]
    data = append(ad, nd)
    print(data)
main()