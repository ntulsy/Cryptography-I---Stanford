__author__ = 'Siyao'

from Crypto.Cipher import AES
from Crypto.Util import Counter

def AES_decrypt_CBC(key, ciphertext):
    IV_decoded, ciphertext_decoded = ciphertext[:32].decode("hex"), ciphertext[32:].decode("hex")
    decryptor = AES.new(key.decode("hex"), AES.MODE_CBC, IV=IV_decoded)
    return decryptor.decrypt(ciphertext_decoded)

def AES_decrypt_CTR(key, ciphertext):
    IV, ciphertext_decoded = ciphertext[:32], ciphertext[32:].decode("hex")
    counter = Counter.new(128, initial_value=long(IV, 16))
    decryptor = AES.new(key.decode("hex"), AES.MODE_CTR, counter=counter)
    return decryptor.decrypt(ciphertext_decoded)

if __name__ == "__main__":
    CBC_key = "140b41b22a29beb4061bda66b6747e14"
    CTR_key = "36f18357be4dbd77f050515c73fcf9f2"
    ciphertexts = ["4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81",
                   "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253",
                   "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329",
                   "770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"]
    print AES_decrypt_CBC(CBC_key, ciphertexts[0])
    print AES_decrypt_CBC(CBC_key, ciphertexts[1])
    print AES_decrypt_CTR(CTR_key, ciphertexts[2])
    print AES_decrypt_CTR(CTR_key, ciphertexts[3])