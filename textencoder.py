# -*- coding: utf-8 -*-
"""
Created on Wed May 21 01:25:41 2025

@author: Sophia Woods
    Project: text_generator_encoder
    File Name: txtencoders.py
    purpose: to convert text into numbers so that an AI model can efficiently interpret and utilize information. ##TEST
"""
# text_encoders.py file content

import string


# TODO: COMMENT: DEF NAME IS Alphabet_encode_Word
def alpha_encoded(word):
    """
    Converts a word into a numerical sum based on the alphabetical position of its letters.
    'a' or 'A' = 1, 'b' or 'B' = 2, etc.
    Example: 'cab' -> 3 + 1 + 2 = 6
    """
    numerical_value = 0
    word = word.lower()

    for char in word:
        if 'a' <= char <= 'z':
            letter_value = ord(char) - ord('a') + 1
            numerical_value += letter_value

    return numerical_value


alpha_encoded
