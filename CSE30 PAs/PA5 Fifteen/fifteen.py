#name: Phil Liu
#PA5 Fifteen
#fifteen.py module

import numpy as np
from random import choice

class Fifteen:
    
    def __init__(self, size = 4):
        self.tiles = np.array([i for i in range(1,size**2)] + [0])
        self.size = size
        self.adj = [[1, 4], [0, 2, 5], [1, 3, 6], [2, 4, 7], [3, 5, 0, 8], [4, 6, 1, 9],
                    [5, 7, 2, 10], [6, 8, 3, 11], [7, 9, 4, 12], [8, 10, 5, 13], [9, 11, 6, 14],
                    [10, 12, 7, 15], [11, 3, 8], [12, 14, 9], [13, 15, 10], [14, 11]]

    def update(self, move):
        if self.is_valid_move(move):
            index_empty = np.where(self.tiles == 0)[0][0]
            index_move = np.where(self.tiles == move)[0][0]
            
            self.tiles[index_empty], self.tiles[index_move] = self.tiles[index_move], self.tiles[index_empty]


    def shuffle(self, steps=100):
        index = np.where(self.tiles == 0)[0][0]
        for _ in range(steps):
            move_index = choice(self.adj[index])
            self.tiles[index], self.tiles[move_index] = self.tiles[move_index], self.tiles[index]
            index = move_index


    def is_valid_move(self, move): 
        index_empty = np.where(self.tiles == 0)[0][0]
        index_move = np.where(self.tiles == move)[0][0]
        
        return index_move in self.adj[index_empty]
    
    def is_solved(self):
        solvedarray = np.arange(1, self.size**2)
        return np.array_equal(self.tiles[:-1], solvedarray)
    
    def draw(self):
        horizontal_line = "+---" * self.size + "+"
        rows = self.tiles.reshape(self.size, self.size)
        output = [horizontal_line]

        for row in rows:
            row_str = "|" + " |".join(f'{tile:2}' if tile != 0 else '  ' for tile in row) + " |"
            output.extend([row_str, horizontal_line])

        print('\n'.join(output))


    def __str__(self):
        string = ''
        for i in range(16):
            if self.tiles[i] == 0:
                string += '   '
            else:
                string += f'{self.tiles[i]:2d} '
            if (i + 1) % 4 == 0:
                string += '\n'
        return string
    

if __name__ == '__main__':

    game = Fifteen()
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_valid_move(15) == True
    assert game.is_valid_move(12) == True
    assert game.is_valid_move(14) == False
    assert game.is_valid_move(1) == False
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14    15 \n'
    game.update(15)
    assert str(game) == ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == True
    game.shuffle()
    assert str(game) != ' 1  2  3  4 \n 5  6  7  8 \n 9 10 11 12 \n13 14 15    \n'
    assert game.is_solved() == False


    game = Fifteen()
    game.shuffle()
    game.draw()
    while True:
        move = input('Enter your move or q to quit: ')
        if move == 'q':
            break
        elif not move.isdigit():
            continue
        game.update(int(move))
        game.draw()
        if game.is_solved():
            break
    print('Game Over!')
    game = Fifteen()
 
    
    