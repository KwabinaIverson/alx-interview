#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """
    `validUTF8` determines if a given data set represents a valid UTF-8 encoding
    
    Arg:
        data (array/list): The data set can contain multiple characters
        adn the data will be represented by a list of integers.
        
    Return: True if data is a valid UTF-8 encoding, else return False.
    """
    num_bytes = 0

    bit7 = 1 << 7
    bit6 = 1 << 6

    for num in data:
        byte = 1 << 7
        if num_bytes == 0:
            while byte & num:
                num_bytes += 1
                byte = byte >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (num & bit7 and not (num & bit6)):
                return False
        num_bytes -= 1
    return num_bytes == 0
