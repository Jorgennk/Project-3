"""
File for Cipher, intended to be a parent class for different ciphering methods
"""

class Cipher:
    """
    Parent class for the different chiperings
    """

    def __init__(self):
        """
        Constructor with the values going to be used later in other ciphering methods
        """
        self.key = ""
        self.message = ""
        self.alphabet = {
            0: "A",
            1: "B",
            2: "C",
            3: "D",
            4: "E",
            5: "F",
            6: "G",
            7: "H",
            8: "I",
            9: "J",
            10: "K",
            11: "L",
            12: "M",
            13: "N",
            14: "O",
            15: "P",
            16: "Q",
            17: "R",
            18: "S",
            19: "T",
            20: "U",
            21: "V",
            22: "W",
            23: "X",
            24: "Y",
            25: "Z"
        }

    def set_key(self, key_to_be_set):
        """
        Sets the current key used for encryption
        :param key_to_be_set: Key to be set
        :return: None
        """
        self.key = int(key_to_be_set)

    def get_key(self):
        """
        Simply returns the current key used for encryption
        :return: The current key
        """
        return self.key

    def get_message(self):
        """

        :return: The current message, either encrypted or not
        """
        return self.message

    def operate_cipher(self):
        """
        Not used, kept it here for reference
        :return:
        """
        pass

    def set_message(self, input_message):
        """
        :param input_message: The message to be set
        :return: None
        """
        self.message = input_message

    def print_message(self):
        """
        Prints the currents message to the console
        :return: None
        """
        print(self.message)
