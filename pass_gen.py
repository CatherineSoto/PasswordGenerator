# This is a python password generator, creates an 8-character and a 16-character random password.
# Figure out on how to take in input from user as the length

"""
NEED TO COMPLETE:
* Create a new password length between 4-50 characters.
* You can choose whether you want to use letters, numbers, and/or symbols.
* Display a warning when none of the options have been selected. Give the user another attempt to click atleast one of them.
"""

# Declarations
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "@%+!#$&?"

# 8-character password generator
all_eight = lower + upper + numbers + symbols
length_eight = 8
eight_pass = "".join(random.sample(all_eight,length_eight))
print("8-character password: " + eight_pass)

# 16-character password
all_sixteen = lower + upper + numbers + symbols
length_sixteen = 16
sixteen_pass = "".join(random.sample(all_sixteen,length_sixteen))
print("16-character password: " + sixteen_pass)

#input("Press ENTER to exit.")
#You must add some sort of indicator to the code to keep the exe from automatically closing the console
