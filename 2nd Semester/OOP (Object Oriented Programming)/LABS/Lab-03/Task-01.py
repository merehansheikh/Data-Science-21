
import random
def status_of_ball():
    status_of_ball = random.randint(0,2)
    return status_of_ball

def run_out_or_not():
    run_out_or_not = random.randint(0,1)
    if run_out_or_not == 0:
        return False
    return True

def type_of_out():
    type_of_out = random.randint(0,2)
    if type_of_out == 0:
        return '.\tR' #run out
    elif type_of_out == 1:
        return '.\tB' #bowled out
    return '.\tC' # catch out

def score():
    return (random.randint(1,6)) 
    # for the random score

def main():
    total_score = 0
    total_wickets = 0
    extra = 0
    print('Type\tScore\tOut')

    for i in range(10):

        s = status_of_ball()
        if s == 0: #in case of normal ball
            print('-', end='\t')
            if run_out_or_not():
                total_wickets += 1
                print(type_of_out())
            else:
                scr = score()
                total_score += scr
                print(scr)
            print()

        elif s == 1: #in case of wide ball
            print('W', end='\t')
            wide_score = random.randint(1,4)
            total_score += wide_score + 1
            extra += 1
            print(wide_score, end='\t')
            if run_out_or_not():
                print('R')
                total_wickets += 1
            print()

        else:
            print('N', end='\t')
            scr = score()
            total_score += scr +2
            extra += 2
            print(scr)
            if run_out_or_not():
                print('.\tR')
                total_wickets += 1
            print()
    print(f'Total Score: {total_score}\t Total Wickets:{total_wickets}\t Extra: {extra}')
main()