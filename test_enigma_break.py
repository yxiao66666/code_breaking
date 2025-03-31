# -*- coding: utf-8 -*-
"""
Create and test an Enigma machine encryption and decoding machine

This code is based on the implementation of the Enigma machine in Python 
called pyEnigma by Christophe Goessen (initial author) and Cédric Bonhomme
https://github.com/cedricbonhomme/pyEnigma

Created on Tue Feb  5 12:17:02 2019

@author: uqscha22
"""
import string
import enigma
import rotor
import time

letters = string.ascii_letters #contains 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
capitalLetters = letters[-26:]
#print(capitalLetters)

ShakesHorribleMessage = "Xm xti ca idjmq Ecokta Rkhoxuu! Kdiu gm xex oft uz yjwenv qik parwc hs emrvm sfzu qnwfg. Gvgt vz vih rlt ly cnvpym xtq sgfvk jp jatrl irzru oubjo odp uso nsty jm gfp lkwrx pliv ojfo rl rylm isn aueuom! Gdwm Qopjmw!"
crib = " Hail Shakes!" 
crib_substring = " Gdwm Qopjmw!" 
print(crib_substring)

##Break the code via brute force search
#INSERT CODE HERE

# Initialize counter variable and time variable
count = 0
start_time = time.time()


# Only ture when a match is found
match_found = False

# Iterate through all possible keys
for rotor_1 in capitalLetters:
    for rotor_2 in capitalLetters:
        for rotor_3 in capitalLetters:
            count += 1
            # Create the Enigma machine with different keys
            engine = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                   rotor.ROTOR_II, rotor.ROTOR_III, key=rotor_1 + rotor_2 + rotor_3,
                                   plugs="AA BB CC DD EE")  # AAA -> AAB -> AAC -> ... -> ZZZ

            # Decrypt the message substring using the current key 
            decrypted_substring = engine.encipher(crib_substring)
            
            print(decrypted_substring)  # decrypted message substring

            # Check if the crib is in the decrypted message substring
            if crib in decrypted_substring:
                print("Decrypted Substring:", decrypted_substring)  # " Hail Shakes!"
                print(rotor_1 + rotor_2 + rotor_3)  # KRT

                match_found = True
                break  # Break if a match is found
        if match_found:
            break
    if match_found:
        break


#Print the Decoded message
#INSERT CODE HERE
engine2 = enigma.Enigma(rotor.ROTOR_Reflector_A, rotor.ROTOR_I,
                                rotor.ROTOR_II, rotor.ROTOR_III, key=rotor_1 + rotor_2 + rotor_3, # must be same key as first enigma machine
                                plugs="AA BB CC DD EE")

message1 = engine2.encipher(ShakesHorribleMessage)
print("Decoded Message:", message1)


# The number of iterations
print("Iteration Times:", count, "times")

# Calculate time taken
end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed Time:", elapsed_time, "seconds")




"""
d)
It takes my computer about 1.7 - 1.8s to do all the calculation. 

Here is my specs during a calculation:

CPU

	13th Gen Intel(R) Core(TM) i5-13420H

	Base speed:	2.10 GHz
	Sockets:	1
	Cores:	8
	Logical processors:	12
	Virtualisation:	Enabled
	L1 cache:	704 KB
	L2 cache:	7.0 MB
	L3 cache:	12.0 MB

	Utilisation	31%
	Speed	2.99 GHz
	Up time	17:14:03:27
	Processes	269
	Threads	4246
	Handles	1102119

In the year 1944, the British used a machine called Colossus which produces a processing speed of roughly 5.8 MHz (Bletchley Park, 2008). 
Since 2.99 GHz = 2990 MHz,
We can roughly calculate the time it would take for Colossus to process calculation be:
1.7 * 1000 = 17000 seconds, 

Which is about 47.22 hours. 


e)
There are 17576 combinations from AAA - ZZZ and it takes my laptop about 1.7 seconds. 
If there are 158962555217826360000 combinations as a Enigma machine does have, 
It is roughly 9.0442965 * 10^15 times larger than 17576 combinations, 
So 9.0442965 * 10^15 * 1.7 = 15.37530405 * 10^15 seconds

It will take my laptop 15.37530405 * 10^15 seconds to complete this job.
Which is about 487547693 years.




Reference

Bletchley Park. (2008, January 27). German Codebreaker receives Bletchley Park Honours. 
Retrieved from Bletchley Park: 
https://web.archive.org/web/20130102214431/http://www.bletchleypark.org.uk/news/docview.rhtm/487682



"""