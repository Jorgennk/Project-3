"""
This is the RSA encryption file
"""

import random

import crypto_utils
from Cipher import Cipher


class RSA(Cipher):
    """
    Class for the RSA encryption
    """

    def __init__(self):
        """
        An RSA constructor with all the necessary constants as described in the task
        """
        super().__init__()
        self.q = crypto_utils.generate_random_prime(8)
        self.p = crypto_utils.generate_random_prime(8)
        self.n = self.q * self.p
        self.s = (self.q - 1) * (self.p - 1)
        self.e = random.randint(3, self.s - 1)

        self.d = crypto_utils.modular_inverse(self.e, 26)

    def test(self):
        """
        ??????
        :return:
        """
        pass


