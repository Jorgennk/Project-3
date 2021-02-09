class Cipher:

    def __init__(self):
        self.key = ""
        self.message = ""
        self.encoded_message = ""
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
            11: "l",
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
        self.key = key_to_be_set

    def get_key(self):
        return self.key

    def operate_cipher(self):
        pass

    def set_message(self, input):
        self.message = input
