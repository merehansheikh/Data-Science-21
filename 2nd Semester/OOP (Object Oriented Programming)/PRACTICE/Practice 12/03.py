def main():
    file = open ('Practice 12.txt', 'r')
    count = 0
    highest_runs = []
    average = []
    i =0
    for line in range(1,1300):
        if (line - 13(i)) == abs(9):
            runs = file.readline()
            # runs.replace('/n', '')
            # runs = int(runs)
            highest_runs.append(runs)
        elif line % 10 == 0:
            avg = file.readline()
            # avg.replace('/n', '')
            # avg = int(runs)
            average.append(avg)
        else:
            file.readline()
    print(highest_runs)
    print(average)
    file.close()
main()