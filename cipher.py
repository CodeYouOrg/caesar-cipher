substitution = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k", 
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r", 
    "n": "s", 
    "o": "t", 
    "p": "u", 
    "q": "v", 
    "r": "w", 
    "s": "x", 
    "t": "y", 
    "u": "z", 
    "v": "a", 
    "w": "b", 
    "x": "c",
    "y": "d", 
    "z": "e", 
}

plain_text = input("Please enter the message you'd like to encrypt: ")
plain_text = plain_text.lower()

encrypted_text = ""
for character in plain_text:
    if character in substitution: 
        character = substitution[character]
    encrypted_text += character

print(encrypted_text)


