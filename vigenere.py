# -*- coding: utf-8 -*-

class vigenereEncoderDecoder:
    """
    This class encodes or decodes using the Vigenère-cipher.
    """
    def __init__(self, message, key):
        self.message = message
        self.key = key

    def __str__(self):
        return f'vigenereEncoderDecoder({self.message}, {self.key})'

    def encode_message(self):
        pass

    def decode_message(self):
        decoded_msg = []

        for i in range(len(self.message)):
            N = ord(self.message[i]) - 97 # ord('a') = 97
            K = ord(self.key[i%len(self.key)]) - 97
            D = N - K
            if D < 0:
                D = D + 26

            decoded_msg.append(chr(D+97))

        return ''.join(decoded_msg)


message = input("Enter the encrypted message: ").lower()
key = input("Enter the cipher keyword: ").lower()

encoder_decoder = vigenereEncoderDecoder(message, key)
print(encoder_decoder)

decoded_msg = encoder_decoder.decode_message()
print(decoded_msg)
