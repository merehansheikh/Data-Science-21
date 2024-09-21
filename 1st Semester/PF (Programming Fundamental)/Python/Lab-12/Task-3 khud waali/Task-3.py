import math
def chng_str(str):
    st = ""
    i = 0
    while (str[i] !=" ") or (str[i + 1] != " "):
        st += str[i]
        i = i + 1
    return st
def chck_name(ct_name):
    f = open('pakcities.txt', 'r')
    cnt = 1
    while cnt<=74:
        if ct_name == chng_str(f.read(20)):
            return cnt
        cnt = cnt + 1
        f.read(16)
    f.close()
def long_lati(name):
    f = open('pakcities.txt', 'r')
    chk = f.read(20)
    ct_nam = chng_str(chk)
    loop = chck_name(ct_nam)
    i = 0
    while i < loop:
        f.readline()
        i = i + 1
    f.seek(20)
    long = f.read(7)
    longitude = float(long)
    f.read(1)
    lat = f.read(7)
    latitude = float(lat)
    return longitude, latitude
    f.close()

def conv(cn):
    r = cn*(math.pi/180)
    return r

def calc_dist(lon_1,lat1,lon_2,lat2):
    R = 6371*10**3
    lati_1=conv(lat1)
    lati_2=conv(lat2)
    dif_lat = conv(lati_2-lati_1)
    dif_long= conv(lon_2-lon_1)

    a = math.sin(dif_lat/2) * math.sin(dif_lat/2) + math.cos(lati_1) * math.cos(lati_2) * math.sin(dif_long/2) * math.sin(dif_long/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R*c
    d = round(d,4)
    d = str(d) +"km"
    return d
def main():
    frst_ct = input("Enter the first city: ")
    scnd_ct = input("Enter the second city: ")
    c1 = frst_ct.lower()
    c2 = scnd_ct.lower()
    file = open("pakcities.txt","r")
    long1, lat1 = long_lati(c1)
    long2, lat2 = long_lati(c2)
    distance = calc_dist(long1, lat1, long2, lat2)
    print("the distance between",c1,"and",c2,"is: ",distance)
    file.close()
main()
