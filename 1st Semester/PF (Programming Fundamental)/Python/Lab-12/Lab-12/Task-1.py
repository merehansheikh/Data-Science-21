import random 
def createNLists(fname):
    f = open(fname + ".txt", "w")
    ran = random.randint(1,9)
    f.write(str(ran)+"\n")
    j = 0
    while j < ran:
        r_no = random.randint(1,9)
        f.write(str(r_no))
        k = 0
        while k < r_no:
            f.write(" ")
            hehe = random.randint(1,2)
            if hehe == 1:
                h1 = random.randint(0,10)
            else:
                h1 = round((random.randint(0,10)/random.randint(1,4)) , 1)
            f.write(str(h1))
            k = k + 1
        j = j + 1
        f.write("\n")

def main():
    no_files = int(input("Enter the number of files: "))
    i = 0
    while i < no_files:
        haha = str(input("Enter the name of file: "))
        createNLists(haha)
        i = i + 1

main()