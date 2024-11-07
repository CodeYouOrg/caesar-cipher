
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
phrase = input("Please enter the phrase you wish to encode: ")
phrase = phrase.lower()
cipherPhrase = ""

for char in phrase:
    if char in alphabet:
        position = alphabet.index(char)
        newPosition = (position + 5) % 26
        cipherPhrase += (alphabet[newPosition])
    else:
        cipherPhrase += char

print(cipherPhrase)
