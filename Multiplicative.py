"""
A Multiplicative way of encrypting a message using simple multiplication on the character values
"""

from Cipher import Cipher


class Multiplicative(Cipher):
    """
    The class for multiplicative encrypting
    """

    def __init__(self):
        """
        Basic constructor with values from super (Cipher)
        """
        super().__init__()

    def encode(self):
        """
        This is a simple function for encoding a string from self.message. It changes the self.message to the encrypted,
        but also prints the last value for confirmation
        :return: None
        """
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
        """
        Finds the number corresponding with the unencrypted letter in the encrypted test
        :param number: the character value of the current letter
        :return: the unencrypted character calue
        """
        for i in range(26 * self.key):
            if number == (i * self.key) % 26:
                return i

    def decode(self):
        """
        Decodes an encrypted string placed in self.message
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

    def print_multi(self):
        """
        Prints the current message
        :return: None
        """
        if self.message:
            print(self.message)
        else:
            print("Nothing decoded yet (multi)")
