# -*- coding: utf-8 -*-

class vigenereDecoder:
    """
    This class decodes a Vigenère-encoded message.
    """
    def __init__(self, encrypted_msg, keyword):
        self.encrypted_msg = encrypted_msg
        self.keyword = keyword

    def decode_message(self):
        for i in range(len(self.encrypted_msg)):
            N = ord(self.encrypted_msg[i]) - 97
            K = ord(self.keyword[i%len(self.keyword)]) - 97
            D = N - K
            if D < 0:
                D = D + 26

            print(i, self.encrypted_msg[i], self.keyword[i%len(self.keyword)], chr(D+97))

encrypted_msg = input("Enter the encrypted message: ").lower()
keyword = input("Enter the cipher keyword: ").lower()

decoder = vigenereDecoder(encrypted_msg, keyword)
decoded_msg = decoder.decode_message()
print(decoded_msg)
