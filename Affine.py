from Cipher import Cipher


class Affine(Cipher):

    def __init__(self):
        super().__init__()
        self.affine_key1 = ""
        self.affine_key2 = ""

    def set_affine_keys(self):
        self.affine_key1 = int(input("Select multiplication key (key1): "))
        self.affine_key2 = int(input("Select addition key (key2): "))

    def encode(self):
        tmp_msg = self.message
        print(self.message)
        self.message = ""
        print(tmp_msg)

        for letter in tmp_msg:
            tmp_liste = list(self.alphabet.values())
            if not letter.upper() == ' ':
                position = tmp_liste.index(letter.upper())
                replacement_num = ((position + self.affine_key2) * self.affine_key1) % 26
                self.message += self.alphabet[replacement_num]
            else:
                self.message += " "

    def find_val(self, number):
        for i in range((26 + self.affine_key2) * self.affine_key1):
            if number == ((i+self.affine_key2) * self.affine_key1) % 26:
                return i

    def decode(self):
        tmp_msg = self.message
        self.message = ""

        for letter in tmp_msg:
            print(letter)
            if not letter == " ":
                position = list(self.alphabet.values()).index(letter.upper())
                self.message += self.alphabet[self.find_val(position)]

            else:
                self.message += " "
