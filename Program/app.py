import tkinter as tk
from functions import use_enigma


def clicked():

    rot_order = rotor_order.get()
    rotors_list = [i.strip() for i in rot_order.split(",")]
    rot_init = rotor_init.get()
    pos_list = [i.strip().upper() for i in rot_init.split(",")]
    reflector = reflect.get().upper()
    plugs = plug.get()
    if plugs:
        init_plug = {
            i.strip()[0].upper(): i.strip()[1].upper() for i in plugs.split(",")
        }
    else:
        init_plug = {}
    user_string = msg.get()

    encrypted = use_enigma(rotors_list, pos_list, init_plug, reflector, user_string)
    decrypted = use_enigma(rotors_list, pos_list, init_plug, reflector, encrypted)

    newWindow = tk.Toplevel(window)
    newWindow.title("Encrypted/Decrypted")

    tk.Label(newWindow, text=f"Msg to be encrypted -> {user_string}", height=2).pack(
        pady=3
    )
    tk.Label(newWindow, text=f"Encrypted msg -> {encrypted}", height=2).pack(pady=3)
    tk.Label(newWindow, text=f"Decrypted msg -> {decrypted}", height=2).pack(pady=3)


window = tk.Tk()
window.geometry("320x220")
window.title("Enigma Simulator")

rotor_label = tk.Label(text="What rotors in what order (1-8):", height=2)
rotor_order = tk.Entry()
rotor_label.grid(row=1, column=1)
rotor_order.grid(row=1, column=2)

init_label = tk.Label(text="Initial Position of rotors (A-Z):", height=2)
rotor_init = tk.Entry()
init_label.grid(row=2, column=1)
rotor_init.grid(row=2, column=2)

reflector_label = tk.Label(text="What reflector (UKW-B,UKW-C):", height=2)
reflect = tk.Entry()
reflector_label.grid(row=3, column=1)
reflect.grid(row=3, column=2)

plug_label = tk.Label(text="Plugboard (AE,UK,OC):", height=2)
plug = tk.Entry()
plug_label.grid(row=4, column=1)
plug.grid(row=4, column=2)

msg_label = tk.Label(text="Msg you wanna encrypt: ", height=2)
msg = tk.Entry()
msg_label.grid(row=5, column=1)
msg.grid(row=5, column=2)


submit = tk.Button(text="Encrypt!", width=10, command=clicked)

submit.grid(columnspan=4)

window.mainloop()
