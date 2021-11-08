import json
from functions import encrypt_rotor, reflector, use_enigma

with open('rotors.json') as f:
    rotor_dict = json.load(f)


def enigma():
    while True:
        print("""
What rotors and in what order do you want them?
Choose between 1-8. Separate them with a comma.""")
        rotors = input('Rotors: ')
        rotors_list = [i.strip() for i in rotors.split(',')]

        print("""
What initial state do you want the rotors to be set (A-Z).
Seperate them with a comma.""")
        rotor_pos = input('Input: ')
        pos_list = [i.strip().upper() for i in rotor_pos.split(',')]

        if len(rotors_list) != len(pos_list):
            print('The positions need to have the same amount than rotors.')
            continue

        reflector = input('\nChoose the reflector (UKW-B/UKW-C): ').upper()

        print("""
Input the initial plugboard settings.
(AE,RK,OT etc etc.). Seperate them with a comma.""")
        user_plug = input('Plugboard: ')
        if user_plug:
            init_plug = {
                i.strip()[0].upper():
                i.strip()[1].upper()
                for i in user_plug.split(',')}
        else:
            init_plug = {}

        print('\nrotors_list -> ', rotors_list)
        print('pos_list -> ', pos_list)
        print('init_plug -> ', init_plug)
        user_choise = input(
            'Correct initial choises?: Y for yes, N for no: ').upper()

        if user_choise == 'N':
            continue
        print('Input the msg you want to encrypt')
        user_string = input('Input: ')
        print('\nBefore encrypting -> ', user_string)
        encrypted = use_enigma(rotors_list,
                               pos_list,
                               init_plug,
                               reflector,
                               user_string)
        print('\nEncrypted message -> ', encrypted)
        decrypted = use_enigma(rotors_list,
                               pos_list,
                               init_plug,
                               reflector,
                               encrypted)
        print('\nDecrypted message -> ', decrypted)

        user_choise = input(
            'Want to continue encrypting?: Y for yes, N for no: ').upper()

        if user_choise == 'N':
            break


def rotors():
    rotor = input(
        'What rotor or reflector do you want to see? (1-8 or UKW-B/C')
    for i in rotor_dict[rotor]:
        print(f'{i} -> {rotor_dict[rotor][i]}')


options = {'R': rotors, 'E': enigma}


def main():
    while True:
        print("""What do you want to do?
E: Use enigma machine
R: See rotors or
X: Exit""")
        option = input('Input: ').upper()
        if option == 'X':
            print('Exiting...')
            break
        options[option]()


if __name__ == '__main__':
    main()
