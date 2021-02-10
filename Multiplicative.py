from Cipher import Cipher
import time


class Multiplicative(Cipher):

    def __init__(self):
        super().__init__()

    def encode(self):
        tmp_msg = self.message
        print(self.message)
        self.message = ""
        print(tmp_msg)

        for letter in tmp_msg:
            tmp_liste = list(self.alphabet.values())
            if not letter.upper() == ' ':
                position = tmp_liste.index(letter.upper())
                replacement_num = (position * self.key) % 26
                self.message += self.alphabet[replacement_num]
            else:
                self.message += " "

    def find_val(self, number):
        for i in range(26 * self.key):
            if number == (i * self.key) % 26:
                return i

    def decode(self):
        tmp_msg = self.message
        self.message = ""

        for letter in tmp_msg:
            if not letter == " ":
                position = list(self.alphabet.values()).index(letter.upper())
                self.message += self.alphabet[self.find_val(position)]

            else:
                self.message += " "

    def print_multi(self):
        if self.message:
            print(self.message)
        else:
            print("Nothing decoded yet (multi)")
