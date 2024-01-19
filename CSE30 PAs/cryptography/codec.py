# author: Phil Liu


import numpy as np

class Codec():
    
    def __init__(self):
        self.name = 'binary'
        self.delimiter = '#' 

    # convert text or numbers into binary form    
    def encode(self, text):
        if type(text) == str:
            return ''.join([format(ord(i), "08b") for i in text])
        else:
            print('Format error')

    # convert binary data into text
    def decode(self, data):
        binary = []        
        for i in range(0,len(data),8):
            byte = data[i: i+8]
            if byte == '00100011': # you need to find the correct binary form for the delimiter
                break
            binary.append(byte)
        text = ''
        for byte in binary:
            text += chr(int(byte,2))       
        return text 

class CaesarCypher(Codec):

    def __init__(self, shift=3):
        self.name = 'caesar'
        self.delimiter = '#'  
        self.shift = shift    
        self.chars = 256      # total number of characters

    # convert text into binary form
    # your code should be similar to the corresponding code used for Codec
    def encode(self, text):
        if type(text) == str:
            data = ''
            for char in text:
                data += chr((ord(char) + self.shift) % self.chars) 
            binary = super().encode(data)   
        return binary
    
    # convert binary data into text
    # your code should be similar to the corresponding code used for Codec
     # shift encoded binary representation back into original binary before running the
    def decode(self, data):
        text = ''
        binary = []  
        decoded = []
        for i in range(0, len(data), 8):
            binary.append(data[i: i+8])
        for i in range(0, len(binary)):
            if ((int(binary[i], 2)) - self.shift) == (ord(self.delimiter)):
                break
            decoded.append(int(binary[i], 2))
        
        unshifted = ((i - self.shift) for i in decoded)
        return text.join(chr(char) for char in unshifted)


# a helper class used for class HuffmanCodes that implements a Huffman tree
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.left = left
        self.right = right
        self.freq = freq
        self.symbol = symbol
        self.code = ''
        
class HuffmanCodes(Codec):

    def __init__(self):
        self.root = None  # Store the root of the Huffman tree
        self.name = 'huffman'
        self.delimiter = '#'  # You can set the delimiter here if needed

    # Helper method to build the Huffman tree from the list of nodes
    def build_tree(self, nodes):
        while len(nodes) > 1:
            nodes = sorted(nodes, key=lambda x: x.freq)
            left = nodes[0]
            right = nodes[1]
            left.code = '0'
            right.code = '1'
            root = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(root)
        return nodes[0]

    # Encode text into Huffman code
    def encode(self, text):
        if type(text) == str:
            data = list(text)
            frequencies = {}
            for char in data:
                if char in frequencies:
                    frequencies[char] += 1
                else:
                    frequencies[char] = 1

            nodes = [Node(freq, char) for char, freq in frequencies.items()]
            root = self.build_tree(nodes)
            self.root = root  # Set the root of the Huffman tree

            encoding_table = {}
            stack = [(root, '')]

            while stack:
                node, code = stack.pop()
                if node.left is None and node.right is None:
                    encoding_table[node.symbol] = code
                if node.left:
                    stack.append((node.left, code + '0'))
                if node.right:
                    stack.append((node.right, code + '1'))

            huffman_encoded_data = ''.join([encoding_table[char] for char in data])

            return huffman_encoded_data
        else:
            print('Format error')

    # Decode Huffman code into text
    def decode(self, data):
        if type(data) == str:
            text = ''
            current_node = self.root  

            for bit in data:
                if bit == '0':
                    current_node = current_node.left
                else:
                    current_node = current_node.right

                if current_node.left is None and current_node.right is None:
                    if current_node.symbol == self.delimiter:
                        break
                    text += current_node.symbol
                    current_node = self.root 
            
            return text
        
        else:
            print('Format error')


# driver program for codec classes
if __name__ == '__main__':
    #text = 'hello' 
    text = 'Casino Royale 10:30 Order martini' 
    print('Original:', text)
    
    c = Codec()
    binary = c.encode(text + c.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary) # should print '011010000110010101101100011011000110111100100011'
    data = c.decode(binary)  
    print('Text:', data)     # should print 'hello'
    
    cc = CaesarCypher()
    binary = cc.encode(text + cc.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)
    data = cc.decode(binary) 
    print('Text:', data)     # should print 'hello'
     
    h = HuffmanCodes()
    binary = h.encode(text + h.delimiter)
    # NOTE: binary should have a delimiter and text should not have a delimiter
    print('Binary:', binary)
    data = h.decode(binary)
    print('Text:', data)     # should print 'hello'

