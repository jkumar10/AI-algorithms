#!/usr/bin/env python2

import sys

# Count # of pieces in given row
#Code written by Dr. David Crandall
def count_on_row(board, row):
    return sum( board[row] )

# Count # of pieces in given column
#Code written by Dr. David Crandall
def count_on_col(board, col):
    return sum( [ row[col] for row in board ] )

# Count total # of pieces on board
#Code written by Dr. David Crandall
def count_pieces(board):
    return sum([ sum(row) for row in board ] )

# Calculate the sum of right diagonal of an element
def right_diagcheck(board,r,c):
    sum2=0
    for i in range(0,N):
        for j in range(0,N):
            if abs(i+j)==abs(r+c):
               sum2=sum2+board[i][j]
    return sum2

# Calculate the sum of left diagonal of an element
def left_diagcheck(board,r,c):
    sum3=0
    for i in range(0,N):
        for j in range(0,N):
            if i-j==r-c:
                sum3 = sum3 + board[i][j]
    return sum3


# Return a string with the board rendered in a human-friendly format
def printable_board(board):
        stra=""
        for i in range(0,N):
            for j in range(0,N):
                flag=False
                for k in range(0, 2 * U, 2):
                    if i==argl[k] and j==argl[k+1]:
                       stra+="X "
                       flag=True
                if flag:
                    continue
                if board[i][j]==0:
                    stra+="_ "
                elif M=='nqueen':
                    stra+="Q "
                elif M=='nrook':
                    stra +="R "
                else:
                    stra +="K "
            stra+="\n"
        return stra


# Add a piece to the board at the given position, and return a new board (doesn't change original)
#Code written by Dr. David Crandall
def add_piece(board, row, col):
    return board[0:row] + [board[row][0:col] + [1,] + board[row][col+1:]] + board[row+1:]

# Checking constraint on positions
def constraint_check(r,c):
    flag=0
    for i in range(0, 2 * U, 2):
        if r==argl[i] and c==argl[i+1]:
            flag=1
            break
    if flag==0:
        return True

# Checking positions where knight can take on
def knight_check(r,c):
    for i in range(0,N):
        for j in range(0,N):
            if (r!=i+2 and c!=j+1) and (r!=i+1 and c!=j+2) and (r!=i-1 and c!=j+2) and (r!=i-2 and c!=j+1) and (r!=i-2 and c!=j-1) and (r!=i-1 and c!=i-2) and (r!=i+1 and c!=j-1) and (r!=i+2 and c!=j-1):
                return True



# Get list of successors of given board state
#Code written by Dr. David Crandall
def successors(board):
    return [ add_piece(board, r, c) for r in range(0, N) for c in range(0,N) ]

#Successor2 : Stopping states with N+1 pieces on them and moves in which no piece is added
def successor2(board):
    list1=[]
    for r in range(0,N):
        for c in range(0,N):
            if M=='nrook':
                if count_on_row(board, r) == 0 and count_on_col(board, c) == 0 and count_pieces(board) < N and board[r][c] == 0 and constraint_check(r,c)==True:
                    list1.append(add_piece(board, r, c))
            if M=='nqueen':
                if count_on_row(board, r) == 0 and count_on_col(board, c) == 0 and count_pieces(board) < N and board[r][c] == 0 and right_diagcheck(board,r,c)==0 and left_diagcheck(board,r,c)==0 and constraint_check(r,c)==True:
                    list1.append(add_piece(board, r, c))
            if M=='nknight':
                if knight_check(r, c) == True and count_pieces(board) < N and board[r][c] == 0 and constraint_check(r,c) == True:
                    list1.append(add_piece(board, r, c))

    return list1

# Finding left most column that is currently empty. In the first for loop the last column c with an entry 1 in it will be
# the left most column. The position of that column is stored in the variable lastcolpos. Piece will be added at lastcolpos+1
# If the board is empty lastcolpos will be 0
def successor3(board):
    list1=[]
    Flag = False
    if count_on_col(board,0) == 1 :
        Flag = True
    lastcolpos=0
    for c in range(0,N):
        if count_on_col(board,c)==1:
            lastcolpos=c

    for ro in range(0,N):
        if M=='nrook':
            if count_on_row(board, ro) == 0 and constraint_check(ro, lastcolpos + 1 if Flag else lastcolpos) == True:
                a = add_piece(board, ro, lastcolpos + 1 if Flag else lastcolpos)
                list1.append(a)
        if M=='nqueen':
            if count_on_row(board, ro) == 0 and right_diagcheck(board,ro,lastcolpos+1 if Flag else lastcolpos)==0 and left_diagcheck(board,ro,lastcolpos+1 if Flag else lastcolpos)==0 and constraint_check(ro, lastcolpos+1 if Flag else lastcolpos) == True:
                a = add_piece(board, ro,lastcolpos+1 if Flag else lastcolpos)
                list1.append(a)

    return list1


# check if board is a goal state
#Code contributed by Dr. David Crandall
def is_goal(board):
    if M=='nrook' or M=='nqueen':
        return count_pieces(board) == N and \
            all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
            all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )
    if M=='nknight':
        return count_pieces(board) == N



# Solve n-queens!
#Code contributed by Dr. David Crandall
def solve(initial_board):
    fringe = [initial_board]
    while len(fringe) > 0:
        if M=='nknight':
            for s in successor2( fringe.pop() ):
                if is_goal(s):
                    return(s)
                fringe.append(s)
        if M=='nrook' or M=='nqueen':
            for s in successor3( fringe.pop() ):
                if is_goal(s):
                    return(s)
                fringe.append(s)
    return False

# This is N, the size of the board. It is passed through command line arguments.
M = (sys.argv[1])
N = int(sys.argv[2])
U = int(sys.argv[3])
argl= [int(sys.argv[3+i+1])-1 for i in range(0,U*2)]
lenarg=len(argl)

# The board is stored as a list-of-lists. Each inner list is a row of the board.
# A zero in a given square indicates no piece, and a 1 indicates a piece.
initial_board = [[0]*N]*N
print ("Starting from initial board:\n" + printable_board(initial_board) + "\n\nLooking for solution...\n")
solution = solve(initial_board)
print (printable_board(solution) if solution else "Sorry, no solution found. :(")


