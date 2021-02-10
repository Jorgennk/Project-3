"""
Hacker
"""
from Cipher import Cipher
from Caesar import Caesar


class Hacker(Cipher):
    """
    Class for hacker
    """

    def __init__(self):
        """
        Basic constructor
        """
        super().__init__()

    def hack(self, myObj):
        """
        A method that hacks an object
        :param myObj:
        :return:
        """
        file1 = open('english_words.txt', 'r')
        Lines = file1.readlines()
        my_words = myObj.get_message().split()
        c = Caesar()
        c.set_message("Testing")
        c.set_key(3)

        for word in my_words:
            count = 0
            # Strips the newline character
            for line in Lines:
                count += 1
                e_word = line.strip()
                encoded_e_word = c.hacker_encode(e_word)
                print("Tested: " + word + "agaist: " + e_word)
                if encoded_e_word == c.hacker_encode(word):
                    print("The key found was: " + str(c.key))
                    print("The matched word was: " + word)
                    return None
