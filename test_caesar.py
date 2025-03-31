# -*- coding: utf-8 -*-
"""
Caesar cypher script

Encode and decode messages by scrambling the letters in your message

Created on Fri Feb  1 23:06:50 2019

@author: shakes
"""
import string

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = "The quick brown fox jumped over the lazy dog" #type your message here
print("Message:", message)

#create the Caesar cypher
offset = 5 #choose your shift
totalLetters = 26
keys = {} #use dictionary for letter mapping
invkeys = {} #use dictionary for inverse letter mapping, you could use inverse search from original dict
for index, letter in enumerate(letters):
    # cypher setup
    if index < totalLetters: #lowercase
        #INSERT CODE HERE
        # Shift the index by 5
        shifted_index = (index + offset) % totalLetters # modulo so stays in abcdefghijklmnopqrstuvwxyz
        # Map the letter to a new letter
        keys[letter] = letters[shifted_index]
        # Map the new letter back to the original letter
        invkeys[letters[shifted_index]] = letter
    else: #uppercase
        #INSERT CODE HERE
        # Same above but uppercase
        shifted_index = (index + offset - totalLetters) % totalLetters # modulo so stays in ABCDEFGHIJKLMNOPQRSTUVWXYZ
        keys[letter] = letters[shifted_index + totalLetters]
        invkeys[letters[shifted_index + totalLetters]] = letter
print("Cypher Dict:", keys)

#encrypt
encryptedMessage = []
for letter in message:
    if letter == ' ': #spaces
        encryptedMessage.append(letter) # keep spaces
    else:
        encryptedMessage.append(keys[letter])
print("Encrypted Message:", ''.join(encryptedMessage)) #join is used to put list into string

#decrypt
decryptedMessage = []
for letter in encryptedMessage:
    if letter == ' ': #spaces
        decryptedMessage.append(letter)
    else:
        decryptedMessage.append(invkeys[letter])
print("Decrypted Message:", ''.join(decryptedMessage)) #join is used to put list into string



