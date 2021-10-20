import string
import json

alphabet = string.ascii_uppercase

# plugboard stuff


def plugboard_dict(plugs):
    temp = {}
    for i in plugs:
        temp[plugs[i]] = i
    plugs.update(temp)
    return plugs

# Rotor stuff


with open('rotors.json') as f:
    rotor_dict = json.load(f)

reverse_rotor = {}
for i in rotor_dict:
    reverse_rotor[i] = dict(
        (y, x) for x, y in rotor_dict[i].items() if not isinstance(y, list))


def encrypt_rotor(rotor_number, value, offset, rot_dict):
    return_value = alphabet[(alphabet.index(
        value) + alphabet.index(offset)) % 26]
    return rot_dict[str(rotor_number)][return_value]


"""
MULTIPLE_ROTORS AND ROTOR_TURN NEEDS TESTING, SO EVERYTHING WORKS WELL!!!!!!!!
"""


def multiple_rotors(rotor_order, init_offset, val, rot_dict):
    for i in range(len(rotor_order)):
        val = encrypt_rotor(rotor_order[i], val, init_offset[i], rot_dict)
    return val


def rotor_turn(rotor_order, init_offset):
    for i in range(len(init_offset)):
        if i == 0:
            init_offset[0] = alphabet[(
                alphabet.index(init_offset[0]) + 1) % 26]
            continue
        if init_offset[i - 1] in rotor_dict[str(rotor_order[i - 1])]['Turn']:
            init_offset[i] = alphabet[(
                alphabet.index(init_offset[i]) + 1) % 26]
    return init_offset

# Reflector


def reflector(rotor, val):
    return rotor_dict[rotor][val]


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
    for letter in msg:
        temp_result = ''
        if letter in plugboard:
            result.append(plugboard[letter])
            continue
        init_offset = rotor_turn(
            rotor_order=rotor_order, init_offset=init_offset)
        temp_result = multiple_rotors(
            rotor_order, init_offset, letter, rotor_dict)
        temp_result = reflector('UKW-B', temp_result)
        temp_result = multiple_rotors(
            rotor_order[::-1], init_offset[::-1], temp_result, reverse_rotor)
        result.append(temp_result)
    return ''.join(result)

# TODO Add functions multiple_rotors and rotor_turn to the main function use_enigma
