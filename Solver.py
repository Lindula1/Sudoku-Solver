import time as t
import sys, subprocess
import os
import random


board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def Solve(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        dumBo = bo
        dumBo[row][col] = i
        print("Solving...")
        printBoard(dumBo)
        t.sleep(0.05)
        os.system("cls||clear")

        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if Solve(bo):
                return True
            bo[row][col] = 0
    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
        
    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
        
    # Check box
    boxX = pos[1] // 3
    boxY = pos[0] // 3

    for i in range(boxY * 3, boxY*3 + 3):
        for j in range(boxX * 3, boxX*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True

def printBoard(bo):
    brd = ""
    for j in range(len(bo)):
        brd += " ".join(str(v) for v in bo[j]) + "\n"
    print(brd, end="\r")
    """
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
        for j in range(len(bo[0])):
            if j  % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")
    """

def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j) #row & column
    
    return None

letters = "abcdefghijklmnopqrstuvwxyz. ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
target = "Generating Sudoku..."
for letter in target:
    for i in letters:
        print(result + i, end="\r")
        if i == letter:
            result += i
            break
        t.sleep(0.002)
        

printBoard(board)
t.sleep(0.7)
Solve(board)
print("Solved")
printBoard(board)
