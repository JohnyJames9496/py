def encrypt(text):
    result = ""

    for char in text:
        if char.islower():  
            shifted = (ord(char) - ord('a') + 3) % 26
            result += chr(shifted + ord('a'))
        else:
            result += char 

    return result


# Example
plaintext = "hello"
ciphertext = encrypt(plaintext)
print("Encrypted:", ciphertext)