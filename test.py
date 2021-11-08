import json
from functions import encrypt_rotor, reflector, use_enigma, multiple_rotors

with open('rotors.json') as f:
    rotor_dict = json.load(f)

with open('reverse_rotors.json') as f:
    reverse_rotor = json.load(f)

testRorder = [1, 1, 1]

test_offset = ['A', 'A', 'A']

test_plug = {'K': 'E', 'T': 'W', 'B': 'R'}

# test_plug = {}

test_string = "What the hell?"

test_refl = 'UKW-B'


# test_string = 'A' * 2000
# encrypted = use_enigma(testRorder, test_offset, {}, test_refl, test_string)

# print(encrypted)

# for i in encrypted:
#     if i == 'A':
#         print('Fail')
#         break

# test_string = "Does this work. This is a test.123324578r)(!/¤)(/"

# print(test_string)
# test = use_enigma(testRorder, test_offset, {}, test_string)
# print(test)
# print(use_enigma(testRorder, test_offset, {}, test))


# test = 'A'
# print(test)
# test = multiple_rotors(testRorder, test_offset, test, rotor_dict, True)
# test = reflector('UKW-B', test)
# test = multiple_rotors(
#     testRorder[::-1], test_offset[::-1], test, reverse_rotor, False)
# print(test)

# test = multiple_rotors(testRorder, test_offset, test, rotor_dict, True)
# test = reflector('UKW-B', test)
# test = multiple_rotors(
#     testRorder[::-1], test_offset[::-1], test, reverse_rotor, False)
# print(test)

print(test_string)
test = use_enigma(testRorder, test_offset, test_plug, test_refl, test_string)
print(test)
print(use_enigma(testRorder, test_offset, test_plug, test_refl, test))


#print(reflector('UKW-B', test_string))


# def test_rotors(tstring):
#     result = ''
#     for letter in tstring:
#         letter = encrypt_rotor(1, letter, 'A', rotor_dict)
#         letter = reflector('UKW-B', letter)
#         letter = encrypt_rotor(1, letter, 'A', reverse_rotor)
#         result += letter
#     return result


# test = test_rotors(test_string)
# print(test)
# print(test_rotors(test))
