import os
import re
if __name__ == '__main__':
    score = 0
    total = 40
    command = 'py' # may need to change to 'py' or 'python3'
    module1 = 'tictac.py'
    module2 = 'testAI.py'
    module3 = 'testMinimax.py'
    module4 = 'testSmartAI.py'
#1 Board
try:
    from board import Board
    print('module board and class Board are implemented +2/2 points')
    score += 2
except:
    print('module board or class Board is not implemented +0/2 points')
#2 Player
try:
    from player import Player
    print('module player and class Player are implemented +2/2 points')
    score += 2
except:
    print('module player or class Player is not implemented +0/2 points')
#3 Board Methods
try:
    board = Board()
    board.get_winner()
    board.set('A1', 'X')
    board.isempty('A1')
    board.isdone()
    print('All Board methods are implemented +4/4 points')
    score += 4
except:
    print('Not all Board methods are implemented +0/4 points')
#4 Player Methods
try:
    player = Player('Bob', 'X')
    player.get_sign()
    player.get_name()
    print('All Player methods are implemented +4/4 points')
    score += 4
except:
    print('Not all Player methods are implemented +0/4 points')
#5 ex1
try:
    os.system(f'{command} {module1} < ex1 > output 2> errors')
    f = open('errors', 'r')
    errors = f.read()
    f.close()
    assert len(errors) == 0
    print('Player runs without errors with input 1 +2/2 points')
    score += 2
except:
    print('Player runs with errors with input 1 +0/2 points')
    print('Player output with input 1 is incorrect +0/2 points')
else:
    try:
        f = open('output', 'r')
        output = f.read()
        f.close()
        f1 = open('ex1.out', 'r')
        out = f1.read()
        f1.close()
        assert re.sub(r'\s', '', output) == re.sub(r'\s', '', out)
        print('Player output with input 1 is correct +2/2 points')
        score += 2
    except:
        print('Player output with input 1 is incorrect +0/2 points')
#6 ex2
try:
    os.system(f'{command} {module1} < ex2 > output 2> errors')
    f = open('errors', 'r')
    errors = f.read()
    f.close()
    assert len(errors) == 0
    print('Player runs without errors with input 2 +2/2 points')
    score += 2
except:
    print('Player runs with errors with input 2 +0/2 points')
    print('Player output with input 2 is incorrect +0/2 points')
else:
    try:
        f = open('output', 'r')
        output = f.read()
        f.close()
        f1 = open('ex2.out', 'r')
        out = f1.read()
        f1.close()
        assert re.sub(r'\s', '', output) == re.sub(r'\s', '', out)
        print('Player output with input 2 is correct +2/2 points')
        score += 2
    except:
        print('Player output with input 2 is incorrect +0/2 points')
#7 AI
try:
    os.system(f'{command} {module2} > output 2> errors')
    f = open('errors', 'r')
    errors = f.read()
    f.close()
    assert len(errors) == 0
    print('AI runs without errors +4/4 points')
    score += 4
except:
    print('AI runs with errors +0/4 points')
    print('AI output is incorrect +0/4 points')
else:
    try:
        f = open('output', 'r')
        output = f.read()
        f.close()
        assert re.findall(r'\bis a winner!|It is a tie!', output) != []
        print('AI output is correct +4/4 points')
        score += 4
    except:
        print('AI output is incorrect +0/4 points')
#8 Minimax
try:
    os.system(f'{command} {module3} > output 2> errors')
    f = open('errors', 'r')
    errors = f.read()
    f.close()
    assert len(errors) == 0
    print('Minimax runs without errors +4/4 points')
    score += 4
except:
    print('Minimax runs with errors +0/4 points')
    print('Minimax output is incorrect +0/8 points')
else:
    try:
        f = open('output', 'r')
        output = f.read()
        f.close()
        assert re.findall(r'It is a tie!', output) != []
        assert re.findall(r'\bis a winner!', output) == []
        print('Minimax output is correct +8/8 points')
        score += 8
    except:
        print('Minimax output is incorrect +0/8 points')

    #9 SmartAI
try:
        os.system(f'{command} {module4} > output 2> errors')
        f = open('errors', 'r')
        errors = f.read()
        f.close()
        assert len(errors) == 0
        print('SmartAI runs without errors +1/1 points')
        score += 1
except:
    print('SmartAI runs with errors +0/1 points')
    print('SmartAI output is incorrect +0/4 points')
else:
    try:
        f = open('output', 'r')
        output = f.read()
        f.close()
        assert re.findall(r'\bis a winner!', output) == []
        assert re.findall(r'It is a tie!', output) != []
        print('SmartAI output is correct +4/4 points')
        score += 4
    except:
        print('SmartAI output is incorrect +0/4 points')

# output results
print(f'\n{score} points out of {total}\n')
with open('tmp', 'w') as f:
    f.write(str(score))