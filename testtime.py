import timeit
import string
import random

##
## This file is for testing the execution time of enigma algorithm
## 

# Initial setup for timeit function, no need to be changed
setup = """
from functions import encrypt_rotor, reflector, use_enigma, multiple_rotors
import json

testRorder = [1, 1, 1]
test_offset = ['A', 'A', 'A']
test_plug = {'K': 'E', 'T': 'W', 'B': 'R'}
test_refl = 'UKW-B'

with open('rotors.json') as f:
    rotor_dict = json.load(f)

with open('reverse_rotors.json') as f:
    reverse_rotor = json.load(f)

test_string = 'TEST_STRING'
"""

# Change these values to
message_length = 100            # Replace with chosen message length to be encrypted
number_of_executions = 100000   # Replace with chosen number, how many times to execute the algorithm in the test

# generating random message with custom length
letters = string.ascii_uppercase
message = ''.join(random.choice(letters) for i in range(message_length))
if message_length < 130:
  print("Message: ",message)
else:
  print("Message:  (too long to show)")

import_setup = setup.replace("TEST_STRING",message)
testcode = "use_enigma(testRorder, test_offset, test_plug, test_refl, test_string)"

print("Running encryption algorithm {} times for a message with length of {}..".format(number_of_executions, len(message)))
time = timeit.timeit(stmt=testcode, setup=import_setup, number=number_of_executions)
timeavgper = float(time / number_of_executions)
print("Total execution time was {}\nAVG time per one execution was {:f}".format(time,timeavgper))