import Cipher


class Multiplicative(Cipher):

    def __init__(self):
        self.multi_msg = ""
        pass

    def encode(self):
        numbers_list = []
        for letter in self.message:
            tmp_num = ord(letter) - 65
            tmp_num = (tmp_num * self.key) % 26
            self.encoded_message += chr(tmp_num + 65)

    def find_val(self, number):
        for i in range(26 * self.key):
            if number == i % 26:
                return i

    def decode(self):
        for letter in self.encoded_message:
            self.multi_msg += chr(self.find_val(ord(letter) - 65))

    def print_multi(self):
        if self.multi_msg:
            print(self.multi_msg)
        else:
            print("Nothing decoded yet (multi)")
