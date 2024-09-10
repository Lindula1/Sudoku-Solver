import time as t
import sys, subprocess
import os
import random

k = 0
base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)
from random import sample
def shuffle(s): return sample(s,len(s)) 
rBase = range(base) 
rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
nums  = shuffle(range(1,base*base+1))

# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]

squares = side*side
empties = squares * 3//4
for p in sample(range(squares),empties):
    board[p//side][p%side] = 0

def Solve(bo):
    find = findEmpty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if Solve(bo):
                return True
            bo[row][col] = 0
        global k
        k += 1
        '''
        print("Solving...")
        printBoard(bo)
        t.sleep(0.008)
        os.system("cls||clear")
        '''
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


def findEmpty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i, j) #row & column
    
    return None

letters = "abcdefghijklmnopqrstuvwxyz. ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ""
target = "Generating Sudoku"
for letter in target:
    for i in letters:
        print(result + i, end="\r")
        if i == letter:
            result += i
            break
        t.sleep(0.002)
        

printBoard(board)
t.sleep(1.3)
Solve(board)
print("Solved in", k, "iterations")
printBoard(board)
