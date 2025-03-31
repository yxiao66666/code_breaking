# -*- coding: utf-8 -*-
"""
Determine the shift of the Caesar Cypher

Created on Sat Feb  2 23:03:02 2019

@author: shakes
"""
from collections import Counter
import string

message = "Zyp cpxpxmpc ez wzzv fa le esp delcd lyo yze ozhy le jzfc qppe Ehz ypgpc rtgp fa hzcv Hzcv rtgpd jzf xplytyr lyo afcazdp lyo wtqp td pxaej hteszfe te Escpp tq jzf lcp wfnvj pyzfrs ez qtyo wzgp cpxpxmpc te td espcp lyo ozye esczh te lhlj Depaspy Slhvtyr" 

# Frequency of each letter
letter_counts = Counter(message)
# Print(letter_counts)

# Find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items(): 
    print(letter, ":", freq) 
    #INSERT CODE TO REMEMBER MAX
    # The letter's frequency is higher than the current maximum frequency, if true then letter now has the maximum frequency
    if freq > maxFreq and letter in string.ascii_lowercase: # Check if lowercase
        maxFreq = freq
        maxLetter = letter

print("Max Ocurring Letter:", maxLetter)

# Predict shift
# Assume max letter is 'e'
letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# Calculating the difference between the most frequent letter and e
shift = ord(maxLetter) - ord('e') #COMPUTE SHIFT HERE
print("Predicted Shift:", shift)


