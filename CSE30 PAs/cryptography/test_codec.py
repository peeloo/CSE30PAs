# CSE30
# PA Steganography
# Driver program to test codecs
if __name__ == '__main__':
    
    score = 0
    total = 18

# test CaesarCypher

    try:
        from codec import CaesarCypher
        text1, text2 = 'hello', 'Casino Royale 10:30 Order martini'
        cc = CaesarCypher()
        binary1 = cc.encode(text1+'#')
        assert binary1 == '011010110110100001101111011011110111001000100110'
        binary2 = cc.encode(text2+'#')
        assert binary2 == '01000110011001000111011001101100011100010111001000100011010101010111001001111100011001000110111101101000001000110011010000110011001111010011011000110011001000110101001001110101011001110110100001110101001000110111000001100100011101010111011101101100011100010110110000100110'
        print('Caesar cypher encoding works +5/5 points')
        score += 5
    except:
        print('Caesar Cypher encoding does not work +0/5 points ')
    try:
        assert cc.decode(binary1) == text1
        assert cc.decode(binary2) == text2
        print('Caesar cypher decoding works +5/5 points')
        score += 4
    except:
        print('Caesar cypher decoding does not work +0/5 points ')

# test HuffmanCodes

    try:
        from codec import HuffmanCodes
        text1 = 'hello'
        h = HuffmanCodes()
        binary1 = h.encode(text1+'#')
        assert binary1 == '11011110100001'
        print('Huffman codes encoding works for a simple input +2/2 points')
        score += 2
    except:
        print('Huffman codes encoding does not work for a simple input +0/2 points ')
    try:
        assert h.decode(binary1) == text1
        print('Huffman codes decoding works for a simple input +3/3 points')
        score += 2
    except:
        print('Huffman codes decoding does not work for a simple input +0/3 points ')

    try:
        text2 = 'Casino Royale 10:30 Order martini'
        h = HuffmanCodes()
        binary2 = h.encode(text2+'#')
        assert binary2 == '011101101011111110000101000011000001001000111011001001010011001101101010010101011000110110111110111010111110011100011011111110011110000111100000'
        print('Huffman codes encoding works +2/2 points')
        score += 2
    except:
        print('Huffman codes encoding does not work +0/2 points ')
    try:
        assert h.decode(binary2) == text2
        print('Huffman codes decoding works +3/3 points')
        score += 3
    except:
        print('Huffman codes decoding does not work +0/3 points ')

# output results        
    print(f'your score is {score} out of {total}')
    with open('tmp', 'w') as f:
        f.write(str(score))
