import string
import json

alphabet = string.ascii_uppercase

# plugboard stuff

# Toimii


def plugboard_dict(plugs):
    temp = {}
    for i in plugs:
        temp[plugs[i]] = i
    plugs.update(temp)
    return plugs

# Rotor stuff


with open('rotors.json') as f:
    rotor_dict = json.load(f)

# Toimii


def encrypt_rotor(rotor_number, value, offset):
    return_value = alphabet[(alphabet.index(
        value) + alphabet.index(offset)) % 26]
    return rotor_dict[str(rotor_number)][return_value]


# Reflector

# Toimii
def reflector(val):
    return alphabet[alphabet.index(val)*-1 - 1]


"""
use_enigma input
Rotor_order: list, with the order of the rotors and what rotors are used
init_offset: list, as the same length as rotor_order, telling what the initial positions for the rotors are.
plugboard: Dict that tells all of the letters that are gonna be bypassed
msg: string, with the message that needs encrypting
"""


def use_enigma(rotor_order, init_offset, plugboard, msg):
    # Making the plugboard to have both of the letters that are connected into the dict.
    plugboard = plugboard_dict(plugboard)
    result = []
    first_rotor = rotor_order.pop(0)
    first_offset = init_offset.pop(0)
    for letter in msg:
        if letter in plugboard:
            result.append(plugboard[letter])
            continue
