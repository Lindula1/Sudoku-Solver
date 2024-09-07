import time as t
import customtkinter as CTK
import tkinter.font as Font

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

class Sudoku(CTK.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) #Useless code left in there (no clue what it does don't know if the code will break if i remove it)
        self.geometry("400x300")
        self.FrA = CTK.CTkFrame(self, width=243, height=243, fg_color="transparent")
        self.FrA.pack(side="left")

    def Main(self):
        self.etyDict = [[],[],[],[],[],[],[],[],[]]
        font = CTK.CTkFont(family="Arial Black", size=12, weight=Font.NORMAL)
        for j in range(9):
            frj = CTK.CTkFrame(self.FrA)
            frj.pack(side="top", pady=2)
            for i in range(9):
                ety = CTK.CTkEntry(frj, height=25, width=25, justify="center", font=font)
                ety.pack(side="left", padx=2)
                ety.insert(0, board[j][i])
                self.etyDict[j].append(ety)
        #t.sleep(2)
        self.after(2000, lambda: self.Solve(board))

    def Solve(self, bo):
        find = self.findEmpty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            if self.valid(bo, i, (row, col)):
                bo[row][col] = i
                self.after(100, lambda: self.etyDict[row][col].delete(0, "end"))
                self.after(100, lambda: self.etyDict[row][col].insert(0,i))
                
                if self.Solve(bo):
                    return True
                bo[row][col] = 0
        return False

    def valid(self, bo, num, pos):
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

    def printBoard(self, bo):
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

    def findEmpty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return(i, j) #row & column
        
        return None    

sudoku = Sudoku()
sudoku.Main()
sudoku.mainloop()