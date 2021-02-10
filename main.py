"""
This is the main programme. It prints out a menu sytem where you can give different inputs

"""
import Caesar
import Multiplicative
import Affine
import Unbreakable
import Hacker
import RSA2

continue_loop = True

while continue_loop:
    print("___________________    _________________")
    print("===.--------.      \__/      .--------.===")
    print("    \___     \_____/  \_____/     ___/")
    print("        \__________\__/__________/")
    print("           Jørgen Menu Template")

    print("Choose 0 for exit")
    print("1 for Caesar")
    print("2 For multiplicative")
    print("3 for affine")
    print("4 for unbreakable")
    print("5 for hacker")
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

    elif choice == "4":
        u = Unbreakable.Unbreakable()
        u.set_keyword(input("Input Keyword: "))
        u.set_message(input("Input message to encode: "))
        u.print_message()
        u.encode()
        u.print_message()
        u.decode()
        u.print_message()

    elif choice == "5":
        c = Caesar.Caesar()
        c.set_key(3)
        c.set_message("Testing")

        h = Hacker.Hacker()
        h.hack(c)











    elif choice == "6":
        print
        "RSA Encrypter/ Decrypter"
        p = int(input("Enter a prime number (17, 19, 23, etc): "))
        q = int(input("Enter another prime number (Not one you entered above): "))
        print
        "Generating your public/private keypairs now . . ."
        public, private = RSA2.generate_keypair(p, q)
        print
        "Your public key is ", public, " and your private key is ", private
        message = input("Enter a message to encrypt with your private key: ")
        encrypted_msg = RSA2.encrypt(private, message)
        print
        "Your encrypted message is: "
        print
        ''.join(map(lambda x: str(x), encrypted_msg))
        print
        "Decrypting message with public key ", public, " . . ."
        print
        "Your message is:"
        print
        RSA2.decrypt(public, encrypted_msg)


#a = Multiplicative.Multiplicative()
#a.set_key(3)
#a.set_message("deeee")
#a.print_multi()
#a.print_message()
#a.encode()
#a.print_multi()
#a.decode()
#a.print_message()