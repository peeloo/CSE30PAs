class Board:
    def __init__(self):
# board is a list of cells that are represented
# by strings (" ", "O", and "X")
# initially it is made of empty cells represented
# by " " strings
        self.sign = " "
        self.size = 3
        self.board = [" " for _ in range(self.size**2)]
        self.winner = ""
    
    def get_size(self):
        return self.size
# optional, return the board size (an instance size)
    
    def get_winner(self):
        return self.winner
# return the winner's sign O or X (an instance winner)
    
    def set(self, cell, sign):
# mark the cell on the board with the sign X or O
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2','C3']
        if cell not in valid_choices:
            print("Invald cell choice.")
            return
        index = valid_choices.index(cell)
        self.board[index] = sign
    
    def isempty(self, cell):
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2','C3']
        if cell not in valid_choices:
            return False
        index = valid_choices.index(cell)     #takes input cell and finds index of that cell in valid_choices
        return self.board[index] == " "
        
# return True if the cell is empty (not marked with X or O)
    
    def isdone(self):
        done = False
        self.winner = ""
# check all game terminating conditions, if one of them is present,
#assign the var done to True
# depending on conditions assign the instance var winner to O or X
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),  
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),  
                          (0, 4, 8), (2, 4, 6)]
        
        for condition in win_conditions:
            a, b, c, = condition
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != " ":
                self.winner = self.board[a]
                done = True
        
        if not done and " " not in self.board:
            done = True
            
        return done
    
    def show(self):
# draw the board
# need to complete the code
        print("   A   B   C  ")
        print(" +---+---+---+")
        print(f"1| {self.board[0]} | {self.board[3]} | {self.board[6]} |")
        print(" +---+---+---+")
        print(f"2| {self.board[1]} | {self.board[4]} | {self.board[7]} |")
        print(" +---+---+---+")
        print(f"3| {self.board[2]} | {self.board[5]} | {self.board[8]} |")
        print(" +---+---+---+")

