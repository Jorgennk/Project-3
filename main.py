import Multiplicative
import Caesar
import Multiplicative
import Affine

continue_loop = True

while continue_loop:
    print("___________________    _________________")
    print("===.--------.      \__/      .--------.===")
    print("    \___     \_____/  \_____/     ___/")
    print("        \__________\__/__________/")
    print("           Jørgen Menu Template")

    print("Choose 1 for Caesar")
    print("2 For multiplicative")
    print("3 for affine")
    choice = input("Your choice: ")

    if choice == "0":
        continue_loop = False

    elif choice == "1":
        c = Caesar.Caesar()
        c.set_key(int(input("Select key: ")))
        message = input("The message you want to encode: ")
        c.set_message(message)
        print("Message is set to: " + c.get_message())
        c.encode()
        print("Encoded it is: " + c.get_message())
        c.decode()
        print("And back again: " + c.get_message())


    elif choice == "2":
        multi = Multiplicative.Multiplicative()
        key_choice = input("Select key: ")
        multi.set_key(key_choice)
        multi.set_message(input("Text to encode: "))
        multi.print_multi()
        multi.print_message()
        multi.encode()
        multi.print_multi()
        multi.decode()
        multi.print_message()

    elif choice == "3":
        a = Affine.Affine()
        a.set_affine_keys()
        a.set_message(input("What you want to write: "))
        a.print_message()
        a.encode()
        a.print_message()
        a.decode()
        a.print_message()


a = Multiplicative.Multiplicative()
a.set_key(3)
a.set_message("deeee")
a.print_multi()
a.print_message()
a.encode()
a.print_multi()
a.decode()
a.print_message()