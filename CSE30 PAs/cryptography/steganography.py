# author: Phil Liu


import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import ceil

# Import the Codec classes
from codec import Codec, CaesarCypher, HuffmanCodes

class Steganography:
    
    def __init__(self):
        self.text = ''
        self.binary = ''
        self.delimiter = '#'
        self.codec = None

    def encode(self, filein, fileout, message, codec):
        image = cv2.imread(filein)
        
        if image is None:
            print(f"Error: Input image file '{filein}' not found.")
            return

        # Calculate the maximum bytes that can be encoded in the image
        max_bytes = image.shape[0] * image.shape[1] * 3 // 8

        # Initialize the codec based on the chosen method
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            self.codec = HuffmanCodes()
        else:
            print(f"Error: Invalid codec '{codec}'")
            return

        # Encode the message using the chosen codec
        binary = self.codec.encode(message + self.delimiter)

        # Check if there are enough available bytes to encode the message
        num_bytes = ceil(len(binary) / 8) + 1
        if num_bytes > max_bytes:
            print("Error: Insufficient bytes in the image!")
        else:
            print("Bytes to encode:", num_bytes)
            self.text = message
            self.binary = binary

            # Embed the binary data into the image using LSB steganography
            self.embed_data(image)

            # Save the steganographic image
            cv2.imwrite(fileout, image)
                   
    def decode(self, filein, codec):
        image = cv2.imread(filein)
        
        if image is None:
            print(f"Error: Input image file '{filein}' not found.")
            return

        flag = True

        # Initialize the codec based on the chosen method
        if codec == 'binary':
            self.codec = Codec()
        elif codec == 'caesar':
            self.codec = CaesarCypher()
        elif codec == 'huffman':
            if self.codec is None or self.codec.name != 'huffman':
                print("A Huffman tree is not set!")
                flag = False
        else:
            print(f"Error: Invalid codec '{codec}'")
            return

        if flag:
            binary_data = self.extract_data(image)  # Extract binary data
            if binary_data is not None:
                self.text = self.codec.decode(binary_data)  # Decode the binary data
                self.binary = binary_data
                print("Decoding successful.")

    def print(self):
        if self.text == '':
            print("The message is not set.")
        else:
            print("Text message:", self.text)
            print("Binary message:", self.binary)

    def show(self, filename):
        plt.imshow(mpimg.imread(filename))
        plt.show()

    def embed_data(self, image):
        binary_data = self.binary
        binary_index = 0

        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                for color_channel in range(3):  # RGB channels
                    if binary_index < len(binary_data):
                        # Convert the pixel value to binary
                        pixel_binary = format(image[row, col, color_channel], '08b')
                        # Replace the least significant bit of the pixel with the binary data
                        pixel_binary = pixel_binary[:-1] + binary_data[binary_index]
                        # Update the pixel value
                        image[row, col, color_channel] = int(pixel_binary, 2)
                        binary_index += 1

    def extract_data(self, image):
        # Extract binary data from the image using LSB steganography
        binary_data = ''
        binary_index = 0

        for row in range(image.shape[0]):
            for col in range(image.shape[1]):
                for color_channel in range(3):  # RGB channels
                    pixel_binary = format(image[row, col, color_channel], '08b')
                    binary_data += pixel_binary[-1]  # Extract the least significant bit
                    binary_index += 1

                # Check for the delimiter to stop extracting
                if binary_index >= 8 and binary_data[-8:] == self.delimiter:
                    binary_data = binary_data[:-8]  # Remove the delimiter
                    return binary_data  # Return the extracted binary data

if __name__ == '__main':
    s = Steganography()

    s.encode('fractal.jpg', 'fractal.png', 'hello', 'binary')
    # NOTE: binary should have a delimiter and text should not have a delimiter
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'

    s.decode('fractal.png', 'binary')
    assert s.text == 'hello'
    assert s.binary == '011010000110010101101100011011000110111100100011'
    print('Everything works!!!')
