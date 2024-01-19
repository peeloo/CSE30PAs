#author: Phil Liu
# DO NOT FORGET TO ADD COMMENTS!!!
#
from stack import Stack
from tree import ExpTree

def infix_to_postfix(expression):
    def precedence(operator):  #setting precedence for all the operators
        if operator == '^':   #will always push
            return 3
        elif operator in ['*', '/']:  #pop if equivalent, push if higher
            return 2
        elif operator in ['+', '-']:  #will always pop
            return 1
        else: #for parentheses, has separate case
            return 0

    def is_higher_precedence(op1, op2):   #checking higher precedence for pop() or push() onto the stack
        return precedence(op1) >= precedence(op2)

    def is_operator(char):   #checking if the operator is a valid operator
        return char in ['+', '-', '*', '/', '^']

    def is_operand(char):   #checking is operand is valid
        return char.isdigit() or char == '.'

    postfix = []   #postfix expression
    stack = Stack()  #operator stack

    for char in expression:   
        if is_operand(char):    #append char if operand is valid
            postfix.append(char)
        elif char == '(':   #adding '(' to stack
            stack.push(char)
        elif char == ')':  # popping out everything out the stack once encounter ')' and adding to postfix
            while not stack.isEmpty() and stack.peek() != '(':
                postfix.append(' ')
                postfix.append(stack.pop())
            stack.pop()  # Pop '(' from the stack
        elif is_operator(char):   #popping out everything into postfix if the operator is higher precedence
            while not stack.isEmpty() and is_higher_precedence(stack.peek(), char) and stack.peek() != '(':
                postfix.append(' ')
                postfix.append(stack.pop())
            stack.push(char)
            postfix.append(' ')

    while not stack.isEmpty():   #popping out rest of the stack into postfix once the expression is completed
        postfix.append(' ')
        postfix.append(stack.pop())

    return ''.join(postfix).strip()



def calculate(infix):
    # call infix -> postfix function (infix is a str)
    postfix = infix_to_postfix(infix).split()
    # use postfix to make a tree -> makeTree()
    tree = ExpTree.make_tree(postfix)
    # evaluate(tree)
    result = ExpTree.evaluate(tree)
    # return the evaluation 
    return result
    

if __name__ == '__main__':
    print('Welcome to Calculator Program!')
    
    while True:
        equation = input('Please enter your expression here. To quit enter \'quit\' or \'q\':')
        if equation == 'quit' or equation =='q':
            break
        result = calculate(equation)
        print(result)
    print('Goodbye!')
