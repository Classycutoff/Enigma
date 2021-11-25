import json

with open('rotors.json') as f:
    rotor_dict = json.load(f)

reverse_rotor = {}
for i in rotor_dict:
    reverse_rotor[i] = dict(
        (y, x) for x, y in rotor_dict[i].items() if not isinstance(y, list))

with open('reverse_rotors.json', 'w+') as f:
    json.dump(reverse_rotor, f)

print(reverse_rotor)


""""
reverse_rotor_dict = {}
for i in rotor_dict:
    reverse_rotor_dict[i] = {(y, x) for y, x in rotor_dict[i]}


print(reverse_rotor_dict)

"""
