import Cipher


class Caesar(Cipher):

    def __init__(self):
        pass

    def encode(self):
        for letter in self.alphabet:
            self.encoded_message += chr(ord(letter) + self.key)

    def decode(self):
        for letter in self.alphabet:
            self.encoded_message += chr(ord(letter) + self.key)

    def print_caesar(self):
        print(self.encoded_message)