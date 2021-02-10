from Cipher import Cipher


class Caesar(Cipher):

    def __init__(self):
        super().__init__()

    def encode(self):
        tmp_msg = self.message
        self.message = ""

        for letter in tmp_msg:
            if not letter == " ":
                position = list(self.alphabet.values()).index(letter.upper())
                print(self.key)
                replacement_num = (position + self.key) % 26
                self.message += self.alphabet[replacement_num]

            else:
                self.message += " "

    def find_val(self, number):
        for i in range(26 + self.key):
            if number == (i + self.key) % 26:
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

    def encode_old(self):
        for letter in self.alphabet:
            self.message += chr(ord(letter) + self.key)

    def decode_old(self):
        for letter in self.alphabet:
            self.message += chr(ord(letter) + self.key)

    def print_caesar(self):
        print(self.message)
