# -*- coding: utf-8 -*-


class vigenereCipherer:
    """
    This class encodes or decodes using the Vigenère-cipher.
    """

    def __init__(self, message, key):
        self.message = message
        self.key = key

    def __str__(self):
        return f"vigenereEncoderDecoder({self.message}, {self.key})"

    def encode_message(self):
        encoded_msg = []

        for i in range(len(self.message)):
            N = ord(self.message[i]) - 97
            K = ord(self.key[i % len(self.key)]) - 97
            D = N + K
            if D > 25:
                D = D - 25

            encoded_msg.append(chr(D + 97))

        return "".join(encoded_msg)

    def decode_message(self):
        decoded_msg = []

        for i in range(len(self.message)):
            N = ord(self.message[i]) - 97  # ord('a') = 97
            K = ord(self.key[i % len(self.key)]) - 97
            D = N - K
            if D < 0:
                D = D + 25

            decoded_msg.append(chr(D + 97))

        return "".join(decoded_msg)


message = input("Enter a message: ").lower()
key = input("Enter a cipher keyword: ").lower()

encoder_decoder = vigenereCipherer(message, key)
print(encoder_decoder)
encoded_message = encoder_decoder.encode_message()
print(f"Encoded message: {encoded_message}")

encoder_decoder = vigenereCipherer(encoded_message, key)
print(encoder_decoder)
decoded_message = encoder_decoder.decode_message()
print(f"Decoded message: {decoded_message}")
