#author: Phil Liu
# DO NOT FORGET TO ADD COMMENTS
#

from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key
    
    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

from stack import Stack  # Assuming you have a stack implementation
from tree import BinaryTree

class ExpTree(BinaryTree):

    @staticmethod
    def make_tree(postfix):
        stack = Stack()

        def is_operator(char):
            return char in ['+', '-', '*', '/', '^']

        for char in postfix:
            if char.replace('.', '', 1).isdigit():  # Check if the char is a number (including floats)
                stack.push(ExpTree(char))
            elif is_operator(char):
                temp = ExpTree(char)
                temp.rightChild = stack.pop()
                temp.leftChild = stack.pop()
                stack.push(temp)

        return stack.pop()

    
    @staticmethod
    def preorder(tree):
        s = ''
        if tree != None:
            s += tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
        return s
    
    @staticmethod
    def inorder(tree):
        s = ''
        if tree != None:
            left_child = ExpTree.inorder(tree.getLeftChild())
            root_val = tree.getRootVal()
            right_child = ExpTree.inorder(tree.getRightChild())

            if root_val in ['+', '-', '*', '/', '^']:
                s += '(' + left_child + root_val + right_child + ')'
            else:
                s += left_child + root_val + right_child

        return s         

    @staticmethod
    def postorder(tree):
        s = ''
        if tree != None:
            s += tree.postorder(tree.getLeftChild())
            s += tree.postorder(tree.getRightChild())
            s += tree.getRootVal()   
        return s
    
    @staticmethod
    def evaluate(tree):
        # base case: if tree is none - return none
        if tree is None:
            return None
        # base case: if root value is a number, we return the number (cast as a float or double)
        else:
            if tree.getRootVal() not in ['+', '-', '*', '/', '^']:
                return float(tree.getRootVal())
            else:   # our root value MUST be an operator at this point
                leftVal = ExpTree.evaluate(tree.getLeftChild())  # evaluate the left (returns a number)
                rightVal = ExpTree.evaluate(tree.getRightChild()) # evaluate the right (returns a number)
                rootVal = tree.getRootVal() # get root value (operand)
                # perform the root value operation on the left and right values, return result
                if rootVal == '+':
                    return leftVal + rightVal
                if rootVal == '-':
                    return leftVal - rightVal
                if rootVal == '*':
                    return leftVal * rightVal
                if rootVal == '/':
                    return leftVal / rightVal
                if rootVal == '^':
                    return leftVal ** rightVal

    def __str__(self):
        return ExpTree.inorder(self)


    
            
   
# # a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    
    postfix = '5.7 2.5 3.1 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5.7+(2.5*3.1))'
    assert ExpTree.inorder(tree) == '(5.7+(2.5*3.1))'
    assert ExpTree.postorder(tree) == '5.72.53.1*+'
    assert ExpTree.preorder(tree) == '+5.7*2.53.1'
    assert ExpTree.evaluate(tree) == 13.45

    postfix = '51 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((51+2)*3)'
    assert ExpTree.inorder(tree) == '((51+2)*3)'
    assert ExpTree.postorder(tree) == '512+3*'
    assert ExpTree.preorder(tree) == '*+5123'
    assert ExpTree.evaluate(tree) == 159
    
    
