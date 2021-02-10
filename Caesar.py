"""
This is the file for the Caesar encryption, only shifting the character value by x places
"""

from Cipher import Cipher


class Caesar(Cipher):
    """
    Caesar class for encryption, me may have came, seen and conquered, but his encryption isn't the best
    """

    def __init__(self):
        """
        Basic constructor with super values
        """
        super().__init__()

    def encode(self):
        """
        Encodes the current message using Caesar ciphering
        :return: None
        """
        tmp_msg = self.message
        self.message = ""

        for letter in tmp_msg:
            if not letter == " ":
                position = list(self.alphabet.values()).index(letter.upper())
                #print(self.key)
                replacement_num = (position + self.key) % 26
                self.message += self.alphabet[replacement_num]

            else:
                self.message += " "

    def find_val(self, number):
        """
        Finds the previous value of the letter before it was encoded
        :param number: number of the current encrypted character
        :return: The number it "used to" be
        """
        for i in range(26 + self.key):
            if number == (i + self.key) % 26:
                return i

    def decode(self):
        """
        This decodes the caesar ciphering using mainly self.find_val(c)
        :return: None
        """
        tmp_msg = self.message
        self.message = ""

        for letter in tmp_msg:
            if not letter == " ":
                position = list(self.alphabet.values()).index(letter.upper())
                self.message += self.alphabet[self.find_val(position)]

            else:
                self.message += " "

    def encode_old(self):
        """
        deprecated
        :return:
        """
        for letter in self.alphabet:
            self.message += chr(ord(letter) + self.key)

    def decode_old(self):
        """
        deprecated
        :return:
        """
        for letter in self.alphabet:
            self.message += chr(ord(letter) + self.key)

    def print_caesar(self):
        """
        prints the current message, not really needed anymore
        :return: None
        """
        print(self.message)

    def hacker_encode(self, string_input):
        """
        Encodes the current message using Caesar ciphering for the hacker compare functions
        :return: None
        """
        tmp_msg = string_input
        string_input = ""

        for letter in tmp_msg:
            if not letter == " ":
                position = list(self.alphabet.values()).index(letter.upper())
                #print(self.key)
                replacement_num = (position + self.key) % 26
                string_input += self.alphabet[replacement_num]

            else:
                string_input += " "

        return string_input
