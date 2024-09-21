from random import randint
def populate(arr, columns, rows):
    i = 0
    while i < rows:
        j = 0
        while j < columns:
            arr[i][j] = randint(10,90)
            j += 1
        i += 1
    return (arr)
def total_budget(arr, cols, rows):
    sum = 0
    i = 0
    while i < rows:
        j = 0
        while j < cols:
            sum += arr[i][j]
            j += 1
        i += 1
    return sum
def mon_max_budget(arr, cols, rows):
    max = 0
    i = 0
    while i < rows:
        sum = 0
        j = 0
        sum += arr[i][j]
        j +=1
        if sum > max:
            max = sum
            month = i
        i += 1
    return month
def total_charity(arr, charity, rows):
    i = 0
    char = 0
    while i < rows:
        char += arr[i][charity]
        i += 1
    return char
def mon_max_trav(arr, trav, rows):
    i = 0
    max_trav = 0
    while i < rows:
        travl = arr[i][trav]
        if max_trav < travl:
            max_trav = travl
            month = i
        i += 1
    return month
def months_name(m):
    months = ['January', 'Feburary', "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    month = months[m]
    return month
def main():
    rows = 12
    x_columns = 5

    budgets_head= ['Travel', 'Eating', 'Books', "Charity", 'Package']
    months = ['Jan', 'Feb', "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    arr = [[0 for i in range (x_columns)] for j in range (rows)]
    populated_arr = populate(arr, x_columns, rows)
    print("Months", end="\t")
    k = 0
    while k < x_columns:
        print(budgets_head[k],end="\t")
        k += 1
    print()
    l = 0
    while l < 12:
        m = 0
        while m < 12:
            print(months[m], end="\t")
            cols = 0
            while cols < 5:
                print(populated_arr[l][cols],end="\t")
                cols += 1
            m += 1
            l += 1
            print()
    
    print("The total budget of the year is", total_budget(arr, x_columns, rows))
    print("The month with the maximum budget is", months_name(mon_max_budget(arr, x_columns, rows)))
    print("The total charity is", total_charity(arr, 3, rows))
    print("The month with the maximum travelling is", months_name(mon_max_trav(arr, 0, rows)))
main()

