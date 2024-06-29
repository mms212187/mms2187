def encrypt(message):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char == "z":
                encrypted_message += "a"
            else:
                encrypted_message += chr(ord(char) + 1)
        else:
            encrypted_message += char
    return encrypted_message


def decrypt(message):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char == "a":
                decrypted_message += "z"
            else:
                decrypted_message += chr(ord(char) - 1)
        else:
            decrypted_message += char
    return decrypted_message


def main():
    original_message = input("Введите исходное сообщение: ")
    encrypted_message = encrypt(original_message)
    print("Зашифрованное сообщение:", encrypted_message)

    encrypted_input = input("Введите зашифрованное сообщение для дешифровки: ")
    decrypted_message = decrypt(encrypted_input)
    print("Дешифрованное сообщение:", decrypted_message)


if __name__ == "__main__":
    main()
