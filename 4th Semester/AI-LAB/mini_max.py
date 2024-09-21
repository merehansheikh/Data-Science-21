def user_1_turn() :
    val = -1
    position = int(input('Enter the position from [1...9]: '))
    while board[position-1] != 0 or position > 9 or position < 1:
        position = int(input("Enter a valid move from [1...9]"))
    
    board[position-1] = -1
    

def mini_max(player):
    brd = analyze_board()
    
    if brd != 0:
        return brd * player
    
    pos = -1; value = -2;
    
    for i in range(9):
        if board[i] == 0:
            board[i] = player
            score = -mini_max(player * -1)
            if score > value:
                value = score
                pos = i
            board[i] = 0
    
    if pos == -1:
        return 0
    return value

def computer_turn():
    position = -1
    val = -2
    
    for i in range(9):
        if board[i] == 0:
            board[i] = 1
            score = -mini_max(-1)
            board[i] = 0
            if score > val:
                val = score
                position = i
    
    board[position] = 1
                

# it is defined on the basis of which player will win the game
def analyze_board(): 
    # flag = False
    winning_pos=[
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
        ]
    for i in range(8):
        if ( board[winning_pos[i][0]] != 0 and
        board[winning_pos[i][0]] == board[winning_pos[i][1]] and
        board[winning_pos[i][1]] == board[winning_pos[i][2]]
        ): 
            return board[winning_pos[i][2]]
    return 0

def print_board():
    # using 1 for O
    # using -1 for X
    hehe = 0
    print("<-- CURRENT STATE -->")
    for i in range(9):
        if hehe == 3:
            hehe = 0
            print('\n')
        if board[i] == 0:
            print(" - ", end=" ")
        if board[i] == 1:
            print(" O ", end=" ")
        if board[i] == -1:
            print(" X ", end=" ")
        hehe +=1

    print('\n')
    
    
    

if __name__ == '__main__':
    # global board
    visited = []
    board = [0 for i in range(9)]
    # board = [0 for i in range(9)]
    flag = True
    print_board()
    
    choice = int(input("Enter when do you want to play 1(st) or 2(nd): "))
    print("Computer : O \t You : X")
    for i in range(9) :
        if analyze_board() != 0:
            break
        if (i + choice) %2 == 0:
            computer_turn()
        else:
            print_board()
            user_1_turn()
        
        
    var = analyze_board()
    if var == 0:
        print_board()
        print("\t--- DRAW ----\t")
    
    elif var == -1:
        print('\t You win, Computer loose !')
    
    else:
        print('\t Computer WINS')
         
        
    