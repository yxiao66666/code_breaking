# -*- coding: utf-8 -*-
"""
@author: Yang Xiao
"""
from collections import Counter
import string

letters = string.ascii_letters       # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_cases = string.ascii_lowercase # contains 'abcdefghijklmnopqrstuvwxyz'
totalLetters = 26

# One remember to look up at the stars and not down at your feet Two never give up work Work gives you meaning and purpose and life is empty without it Three if you are lucky enough to find love remember it is there and dont throw it away Stephen Hawking
encryptedMessage = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr"
# The quick brown fox jumped over the lazy dog
encryptedMessage2 = "Ymj vznhp gwtbs ktc ozruji tajw ymj qfed itl"

# Frequency of each letter
letter_counts = Counter(encryptedMessage)

# Find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    # The letter's frequency is higher than the current maximum frequency, if true then letter now has the maximum frequency
    if freq > maxFreq and letter in lower_cases: # Check if lowercase
        maxFreq = freq
        maxLetter = letter

print("Max Occurring Letter:", maxLetter) # p as seen in test_caesar_break.py

# Predict shift
shift = ord(maxLetter) - ord('e')
print("Predicted Shift:", shift) # 11 as seen in test_caesar_break.py

# Decrypt with predicted shift
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ':  # Spaces
        decryptedMessage.append(letter)
    else:
        if letter.islower():  # Lowercase
            # Calculate the index of the new letter after shifting
            shifted_index = (letters.index(letter) - shift) % totalLetters
            # Append the decrypted letter to the message
            decryptedMessage.append(letters[shifted_index])
        elif letter.isupper():  # Uppercase
            # Same above but uppercase
            shifted_index = (letters.index(letter.lower()) - shift) % totalLetters
            decryptedMessage.append(letters[shifted_index + totalLetters].upper())

print("Decrypted Message:", ''.join(decryptedMessage))  # join is used to put list into string


