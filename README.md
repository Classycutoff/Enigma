# Enigma

This is for algorithms course, to recreate the enigma machine with code.

For it we need:

- Plugboard.
- Different kinds of rotors that you can choose the order and encryption method.
- Reflector at the end to send it back switched, so A becomes Z, B becomes Y etc. Then the signal goes through the rotors again.
- Interface maybe, terminal will do if it is clear enough.

If you need to decode a msg, you just put the same initial values, and it will return the message.

## Reflector

Basically just switches the alphabet[n] character to alphabet[-n-1] character. Easy to implement.

## Plugboard

Even easier, if the char is in connected to the plugboard, both of them will switch places in the end result.

## Rotors

We're using the naval version of the enigma machine, which had eight different rotors, and could house four at the same time.

### Stepping

How to step with code?

Different rotors step in different intervals.

| Rotor | Turnover Position(s) |
| ----- | -------------------- |
| 1     | R                    |
| 2     | F                    |
| 3     | W                    |
| 4     | K                    |
| 5     | A                    |
| 6-8   | A and N              |

This is where each rotor type allowed the next one to move.

First one always turns. Each next one relies on the previous one to turn at designated spots told in the table. 

#### Double-stepping


*If, in moving forward, the ratchet of rotor three was engaged, rotor two would move again on the subsequent keystroke, resulting in two consecutive steps.*

### Amount of rotors

Depends, earlier it was three, but was further increased to four. Might do a rotor function, which takes in a list of the rotors, and prosesses the data accordingly, so you could have theoretically a twelve rotor enigma machine.

## Rotor rambling

So the rotors have a encrypting that doesn't change. what does change is the offset that the letters come in. So if the rotor is set to A, it will take all the letters and encode them normally. But if it is B, it will move them up by one etc etc... 

So once I have these encoding in place, all I need to do is offset them by the specific given value. But we first need to turn it into an index of the alphabet. Fortunately I'm only working in uppercase, and I've already got the list in the functions.py file. So the function rotor might go like this:

```python
encrypt_rotor(rotor_number -> int, value -> str, offset -> str):
    return_value = alphabet[(alphabet.index(value) + alphabet.index(offset)) % 26]
    return rotors[rotor_number][return_value] 
```

## TODO

Every piece is here, but just need to combine them. Important thing that I need to implement is the reverse rotors, though that will be easy, just reverse lists of rotor_order and init_offset.

The only thing really missing is if the rotors move before they give the values or after, but that is easy to implement after I get the knowledge. It also doesn't effect the functionality of the machine, it will just annoy me.


## Weaknesses

- The char cannot map into itself apparently.

## Links

- [Brilliant brakedown](https://brilliant.org/wiki/enigma-machine/)
- [Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine#:~:text=The%20Enigma%20has%20an%20electromechanical,illuminated%20at%20each%20key%20press.)
-[Enigma rotor details](https://en.wikipedia.org/wiki/Enigma_rotor_details)
