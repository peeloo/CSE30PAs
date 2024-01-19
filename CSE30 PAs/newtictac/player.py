from random import choice

class Player:
    def __init__(self, name, sign, board=None):
        self.name = name # player's name
        self.sign = sign # player's sign O or X
    def get_sign(self):
        return self.sign
# return an instance variable sign
    def get_name(self):
        return self.name
# return an instance variable name
    def choose(self, board):
# prompt the user to choose a cell
# if the user enters a valid string and the cell on the board is empty,
#update the board
# otherwise print a message that the input is wrong and rewrite the
#prompt
# use the methods board.isempty(cell), and board.set(cell, sign)
        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2','C3']
        while True:
            cell = input(f'\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]:\n').upper()
            if cell in valid_choices :
                if board.isempty(cell):
                    board.set(cell, self.sign)
                    break
                else:
                    print("You did not choose correctly.")
            else:
                print("You did not choose correctly.")

class AI(Player): 
    def __init__(self, name, sign, board = None):
        super().__init__(name, sign, board)
        self.valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2','C3'] #redefining valid choices for a new object
    
    def choose(self, board):
        if self.valid_choices:   #if valid_choices is not empty
            empty_choices = [cell for cell in self.valid_choices if board.isempty(cell)]
            if empty_choices:    #if there are valid empty cells on the board
                rand_cell = choice(empty_choices)
                board.set(rand_cell, self.sign)
                self.valid_choices.remove(rand_cell)
        

class MiniMax(AI):
    def __init__(self, name, sign, board = None):
        super().__init__(name, sign, board)
        self.valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2','C3']
    
    def choose(self, board):
       
            moves = {}
            for move in self.valid_choices:
                if board.isempty(move):
                    board.set(move, self.sign)
                    score = self.minimax(board, False)
                    board.set(move, " ")  
                    moves[score] = move

            best_score = max(moves.keys())   #getting the best move available 
            best_move = moves[best_score]

            board.set(best_move, self.sign)   # making the best mvoe
            self.valid_choices.remove(best_move)

    def minimax(self, board, maximize):
        if board.isdone():
            if board.get_winner() == self.sign:
                return 1  # self wins
            elif board.get_winner() != self.sign and board.get_winner() != "":
                return -1  # opponent wins
            else:
                return 0   #tie

        if maximize:
            max_score = -float("inf")
            for move in self.valid_choices:
                if board.isempty(move):
                    board.set(move, self.sign)
                    score = self.minimax(board, False)
                    board.set(move, " ")  
                    max_score = max(score, max_score)
            return max_score
        else:
            min_score = float("inf")
            for move in self.valid_choices:
                if board.isempty(move):
                    board.set(move, self.get_opponent_sign())
                    score = self.minimax(board, True)
                    board.set(move, " ")  
                    min_score = min(score, min_score)
            return min_score

    def get_opponent_sign(self):
        return "O" if self.sign == "X" else "X"

class SmartAI(AI):
    def choose(self, board):
        
        cell = self.find_best_move(board)
        board.set(cell, self.sign)

    def find_best_move(self, board):

        for cell in self.get_empty_cells(board):
            board.set(cell, self.sign)
            if board.isdone() and board.get_winner() == self.sign:
                board.set(cell, " ") 
                return cell
            board.set(cell, " ") 

        opponent_sign = "X" if self.sign == "O" else "O"
        for cell in self.get_empty_cells(board):
            board.set(cell, opponent_sign)
            if board.isdone() and board.get_winner() == opponent_sign:
                board.set(cell, " ")  
                return cell
            board.set(cell, " ")  

        # Start at positions with high probability of winning (center or corners)
        preferred_cells = ["B2", "A1", "A3", "C1", "C3"]
        for cell in preferred_cells:
            if board.isempty(cell):
                return cell

        # If none of the above conditions are met, choose an empty cell randomly
        empty_cells = self.get_empty_cells(board)
        return choice(empty_cells)

    def get_empty_cells(self, board):
        return [cell for cell in ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"] if board.isempty(cell)]

