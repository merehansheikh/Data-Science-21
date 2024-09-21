def Grade(total):
    if total>=85:
        return "A+"
    elif total>=80 and total<=84:
        return "A-"
    elif total>=75 and total<=79:
        return "B+"
    elif total>=70 and total<=74:
        return "B"
    elif total>=65 and total<=69:
        return "B-"
    elif total>=61 and total<=64:
        return "C+"
    elif total>=58 and total<=60:
        return "C"
    elif total>=55 and total<=57:
        return "C-"
    elif total>=50 and total<=54:
        return "D"
    else:
        return "F"

def main():
    f = open('result_data.txt', 'r')
    g = open('result_report.txt', 'w')
    
    header = "\tSubject\tSessional\tMidterm\tFinal\tTotal\tGrade "+"\n"
    f.readline()
    f.readline()
    
    count = 1
    for i in range(9):
        roll_name= str(f.read(42))
        crs = str(f.read(3))
        f.read(4)
        md = f.read(2)
        f.read(1)
        ss = f.read(2)
        f.read(1)
        fn = f.read(2)
        f.read(1)
        total = int(md) + int(ss) + int(fn)
        grd = Grade(int(total))
        line = "\t"+str(crs)+"\t\t"+str(ss)+"\t\t\t"+str(md)+"\t\t"+str(fn)+"\t\t"+str(total)+"\t\t"+str(grd)+"\n"
        rl_nm = str(count)+"."+str(roll_name)+"\n"
        g.write(rl_nm)
        g.write(header)
        g.write(line)

        roll_name= str(f.read(42))
        crs = str(f.read(2))
        f.read(5)
        md = f.read(2)
        f.read(1)
        ss = f.read(2)
        f.read(1)
        fn = f.read(2)
        f.read(1)
        total = int(md) + int(ss) + int(fn)
        grd = Grade(int(total))
        line = "\t"+str(crs)+"\t\t"+str(ss)+"\t\t\t"+str(md)+"\t\t"+str(fn)+"\t\t"+str(total)+"\t\t"+str(grd)+"\n"
        g.write(line)

        roll_name= str(f.read(42))
        crs = str(f.read(3))
        f.read(4)
        md = f.read(2)
        f.read(1)
        ss = f.read(2)
        f.read(1)
        fn = f.read(2)
        f.read(1)
        total = int(md) + int(ss) + int(fn)
        grd = Grade(int(total))
        line = "\t"+str(crs)+"\t\t"+str(ss)+"\t\t\t"+str(md)+"\t\t"+str(fn)+"\t\t"+str(total)+"\t\t"+str(grd)+"\n"
        g.write(line)
        g.write("\n")
        count = count +1
    f.close()
    g.close()
main()
