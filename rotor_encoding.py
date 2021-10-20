# This is used for coding the rotors

import string
import json

alphabet = string.ascii_uppercase

rotor_nmbr = input('Which number rotor(1-8): ')

user_inp = input('Rotor string for encoding: ')

result = {rotor_nmbr: {}}

for i in range(len(alphabet)):
    result[rotor_nmbr][alphabet[i]] = user_inp[i]

with open('rotors.json', 'r+') as f:
    data = json.load(f)
    data.update(result)
    f.seek(0)
    json.dump(data, f)
