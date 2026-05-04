def decrypt(text):
    result = ""

    for char in text:
        if char.islower():
            shifted = (ord(char) - ord('a') - 3) % 26
            result += chr(shifted + ord('a'))
        else:
            result += char

    return result

ciphertext = "khoor"
plaintext = decrypt(ciphertext)
print("Decrypted:", plaintext)