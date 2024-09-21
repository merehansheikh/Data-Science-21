def sum_Array(arr,size):
    i = 0
    Sum = 0
    while i < size:
        Sum = Sum + arr[i]
        i=i+1
    return Sum

def average(Sum, size):
    avrg = Sum / size
    return avrg

def count_AN(arr, size, avrg):
    m=0
    c=0
    while m < size:
        if arr[m]> avrg:
            c = c + 1
        m = m + 1
    return c

def createArray():
    siz = int(input("Enter the size of array you want to create: "))
    a= [0] * siz
    f=0
    while f< siz:
        a[f] = int(input("Enter the values: "))
        f=f+1
    return a, siz

def main():
    arrayA, size  = createArray()
    sumarray = sum_Array(arrayA, size)
    print("The sum of all of the values present in array is: ", sumarray)
    print()
    avrg = average(sumarray,size)
    print("The average of all of the values present in array is: ", avrg)
    print()
    count = count_AN(arrayA, size, avrg)
    print("The count of all of the values present in array is: ", count)
main()
