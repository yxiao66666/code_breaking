from collections import Counter
import string


# Define the intercepted message
encrypted_message = "19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11"

# Function to decrypt message with a Caesar Cipher given a shift value
def decrypt_message_caesar(message, shift):
    decrypted_message = ""
    for num in message.split():
        decrypted_char = chr((int(num) - shift - 1) % 26 + 65)  # Decrypt using Caesar Cipher
        decrypted_message += decrypted_char
    return decrypted_message

# Attempt decryption with different shift values
for shift in range(1, 26):
    decrypted_message = decrypt_message_caesar(encrypted_message, shift)
    print(f"Shift {shift}: {decrypted_message}")


letters = string.ascii_letters  # contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
totalLetters = 26

encryptedMessage = "TRRTOUXSTIMQTIDVIZSOSGDSIPSWSL"

# Frequency of each letter
letter_counts = Counter(encryptedMessage)

# Find max letter
maxFreq = -1
maxLetter = None
for letter, freq in letter_counts.items():
    # The letter's frequency is higher than the current maximum frequency, if true then letter now has the maximum frequency
    if freq > maxFreq:
        maxFreq = freq
        maxLetter = letter

print("Max Occurring Letter:", maxLetter) 

# Predict shift
shift = ord(maxLetter) - ord('E')
print("Predicted Shift:", shift) 

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

print("Decrypted Message:", ''.join(decryptedMessage))  





"""
ChatGPT Reference:
https://chat.openai.com/share/c62a5558-5d53-4dd3-a1c9-adc9caed67ed



You: 

Details: 
A number of sophisticated encryption schemes can be broken with some simple prior knowledge of the context in which the message was composed, but without knowing anything about the encryption scheme or device.
Crack the following message intercepted by the United States navy that was addressed to a Japanese naval officer in 1941 to reveal its contents. It is actually doable by hand, but you may use Python as well.

19 17 17 19 14         20 23 18 19 8        12 16 19 8 3       21 8 25 18 14       18 6 3 18 8       15 18 22 18 11

could they have shifted the letters using Caesar Cipher?


ChatGPT:
Yes, that's a possibility. A Caesar Cipher involves shifting each letter in the plaintext by a fixed number of positions down or up the alphabet. Given the historical context, it's a reasonable assumption to try.

Let's write a Python script to attempt to decrypt the message using a Caesar Cipher with different shift values where we try all possible combinations of substitution keys until we find a meaningful decryption. We'll start by trying the most common letter frequencies in English.

# Define the intercepted message
encrypted_message = "19 17 17 19 14 20 23 18 19 8 12 16 19 8 3 21 8 25 18 14 18 6 3 18 8 15 18 22 18 11"

# Function to decrypt message with a Caesar Cipher given a shift value
def decrypt_message_caesar(message, shift):
    decrypted_message = ""
    for num in message.split():
        decrypted_char = chr((int(num) - shift - 1) % 26 + 65)  # Decrypt using Caesar Cipher
        decrypted_message += decrypted_char
    return decrypted_message

# Attempt decryption with different shift values
for shift in range(1, 26):
    decrypted_message = decrypt_message_caesar(encrypted_message, shift)
    print(f"Shift {shift}: {decrypted_message}")

This script will try decrypting the intercepted message using Caesar Cipher with shift values ranging from 1 to 25. You can then examine the output to see if any of the decrypted messages are meaningful English text. The correct shift value should reveal a coherent message.

Let's run the script and see if we can find a meaningful decryption.

You:
Shift 1: RPPRMSVQRGKORGBTGXQMQEBQGNQUQJ
Shift 2: QOOQLRUPQFJNQFASFWPLPDAPFMPTPI
Shift 3: PNNPKQTOPEIMPEZREVOKOCZOELOSOH
Shift 4: OMMOJPSNODHLODYQDUNJNBYNDKNRNG
Shift 5: NLLNIORMNCGKNCXPCTMIMAXMCJMQMF
Shift 6: MKKMHNQLMBFJMBWOBSLHLZWLBILPLE
Shift 7: LJJLGMPKLAEILAVNARKGKYVKAHKOKD
Shift 8: KIIKFLOJKZDHKZUMZQJFJXUJZGJNJC
Shift 9: JHHJEKNIJYCGJYTLYPIEIWTIYFIMIB
Shift 10: IGGIDJMHIXBFIXSKXOHDHVSHXEHLHA
Shift 11: HFFHCILGHWAEHWRJWNGCGURGWDGKGZ
Shift 12: GEEGBHKFGVZDGVQIVMFBFTQFVCFJFY
Shift 13: FDDFAGJEFUYCFUPHULEAESPEUBEIEX
Shift 14: ECCEZFIDETXBETOGTKDZDRODTADHDW
Shift 15: DBBDYEHCDSWADSNFSJCYCQNCSZCGCV
Shift 16: CAACXDGBCRVZCRMERIBXBPMBRYBFBU
Shift 17: BZZBWCFABQUYBQLDQHAWAOLAQXAEAT
Shift 18: AYYAVBEZAPTXAPKCPGZVZNKZPWZDZS
Shift 19: ZXXZUADYZOSWZOJBOFYUYMJYOVYCYR
Shift 20: YWWYTZCXYNRVYNIANEXTXLIXNUXBXQ
Shift 21: XVVXSYBWXMQUXMHZMDWSWKHWMTWAWP
Shift 22: WUUWRXAVWLPTWLGYLCVRVJGVLSVZVO
Shift 23: VTTVQWZUVKOSVKFXKBUQUIFUKRUYUN
Shift 24: USSUPVYTUJNRUJEWJATPTHETJQTXTM
Shift 25: TRRTOUXSTIMQTIDVIZSOSGDSIPSWSL


"""