def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text


user_input = input("Please enter a sentence: ")
shift = 5
result = caesar_cipher(user_input, shift)
print("The encrypted sentence is:", result)
