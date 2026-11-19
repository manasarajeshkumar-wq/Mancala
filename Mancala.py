

##func1:importing files
def import_board(filename):
    file = open(filename, "r")
    lines = file.readlines()
    file.close()
    board = []
    for line in lines:
            number = int(line.strip())                  #adding
            board.append(number)
    if len(board) % 2 != 0:                           #checking for legal board(even)
            return False
    for number in board:                              #checking for legal board(negative)
        if number < 0:
            return False

    return board

##func2:visuals
def show_board(board):
    print("   ", end="")
    for i in range(1,len(board)//2):                      #player 1 wells
            print(board[i], end=" ")
    print("")
    print(board[0], " " * len(board)*2, board[len(board)//2])   #storage (both players)
    print("   ", end="")
    for i in range(len(board)-1,(len(board)//2),-1):         #player 2 wells
            print(board[i], end=" ")

##func3:score board
def score(board):
    player1_score=0
    player2_score=0
    for i in range(0,len(board)//2):
        player1_score+=board[i]                       #adding player 1 storage and wells
    for i in range(len(board)//2, len(board)):
        player2_score+=board[i]                       #adding player 2 storage and wells
    return(player1_score, player2_score)

##function for moving(not in instructions)
def moveccw(board,index,beads,skipindex  ):
    for j in range(index , -1, -1):
        if j != skipindex: #skips the storage 0 and len(board)//2
            board[j]+=1    #adding beads to wells
            beads-=1
        index =j
        if beads <= 0 or index==0:   #when total bead count is over
            return(beads,index)
##func4:movement
def move(board,index):
    if index<=0 or index==len(board)//2 or index>=len(board) or board[index]==0:
        return(board,-1)
    beads = board[index]
    board[index]=0
    if index>0 and index<len(board)//2: #player1
        index -=1
        beads,index = moveccw(board,index,beads,len(board)//2)
        while beads > 0:
            beads,index = moveccw(board,len(board)-1,beads,len(board)//2)

    if index==0:             #playagain
            return (board, 1)
        elif index<len(board)//2 and board[index] == 1 and board[len(board)-index]>0:   #bead ends in empty well of own side
            board[0]+=board[len(board)-index] #move beads to own storage (player1=0)
            board[index]=0
            board[len(board)-index]=0
        return (board, 0)


    else:                              #player 2
        index -=1
         beads,index = moveccw(board,index,beads,0)
while beads > 0:    #wrap around to the other side
            beads,index = moveccw(board,len(board)-1,beads,0)

        if index == len(board)//2:
            return (board,1)      #playagain
        elif index>len(board)//2 and board[index] == 1 and board[len(board)-index]>0:  #ends in empty well own side
            board[len(board)//2]+=board[len(board)-index] #move beads to own storage (player2=0)
            board[index]=0
            board[len(board)-index]=0
        return (board, 0) #turn over

import_board()












