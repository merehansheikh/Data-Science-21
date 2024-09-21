import math

def rplc_space(ct):

    c = ''
    i = 0

    while i < len(ct):
        if ct[i] == ' ':
            c += "-"
        else:
            c += ct[i]
        i += 1

    return c


def file_open():

    f = open("pakcities.txt","r")
    flag = 0

    list_1=[]
    list_2=[]

    for index in f:
        list_1=index.replace("\n","")
        list_2.append(list_1.split(" "))
    f.close()

    return list_2


def conversion(a):

    r = float(a)*(math.pi/180)

    return r


def calc_dist(long1,lat1,long2,lat2):

    R = 6371*10**3

    long_1=conversion(long1)
    lati_1=conversion(lat1)
    long_2=conversion(long2)
    lati_2=conversion(lat2)
    diff_lat = lati_2-lati_1
    diff_long= long_2-long_1

    a = math.sin(diff_lat/2) * math.sin(diff_lat/2) + math.cos(lati_1) * math.cos(lati_2) * math.sin(diff_long/2) * math.sin(diff_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R*c
    d = d/(10**c)
    d = round(d,4)
    d = str(d) +"km"

    return d


def chk(list,ct):

    for i in range(0,len(list)):

        if ct == list[i][0]:
            return list[i]


def main():

    frst_ct = input("Enter the first city: ")
    scnd_ct = input("Enter the second city: ")

    c1 = frst_ct.lower()
    ct_1 = rplc_space(c1)

    c2 = scnd_ct.lower()
    ct_2 = rplc_space(c2)

    listg = file_open()

    check1 = chk(listg,ct_1)
    check2 = chk(listg,ct_2)

    long_1,lati_1 = check1[-2],check1[-1]
    long_2,lati_2 = check2[-2],check2[-1]
    d = calc_dist(long_1,lati_1,long_2,lati_2)
    print("The distance between",c1,"city and",c2,"city is: ",d)

main()


