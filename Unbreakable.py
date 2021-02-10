"""
Problem 4, the unbreakable encryption that consists of caesar + multiplication encryption
"""

from Cipher import Cipher


class Unbreakable(Cipher):
    """
    Unbreakable class which inherits from Cipher
    """

    def __init__(self):
        """
        Basic constructor
        """
        super().__init__()
        self.keyword = ""
        self.keyword_numbers = []

    def set_keyword(self, keyword):
        """
        This methdo encrypts by using a word, hence it needs it's own way of creating a key
        :param keyword: Keyword used for encryption
        :return: None
        """
        self.keyword = keyword

    def encode(self):
        """
        Encrypts the current message
        :return: None
        """
        tmp_message = self.message
        self.message = ""

        for letter in self.keyword:
            letter_number = list(self.alphabet.values()).index(letter.upper())
            self.keyword_numbers.append(letter_number)

        iterator = 0
        for letter in tmp_message:
            original_value = list(self.alphabet.values()).index(letter.upper())
            sum_current_letter = original_value + self.keyword_numbers[(iterator % len(self.keyword))]
            self.message += self.alphabet[sum_current_letter % 26]
            iterator += 1

    def decode(self):
        """
        Decodes the encrypted message into understandable text
        :return: None
        """
        tmp_message = self.message
        self.message = ""

        for letter in self.keyword:
            letter_number = list(self.alphabet.values()).index(letter.upper())
            self.keyword_numbers.append(letter_number)

        iterator = 0
        for letter in tmp_message:
            original_value = list(self.alphabet.values()).index(letter.upper())
            sum_current_letter = original_value - self.keyword_numbers[(iterator % len(self.keyword))]
            self.message += self.alphabet[sum_current_letter % 26]
            iterator += 1
