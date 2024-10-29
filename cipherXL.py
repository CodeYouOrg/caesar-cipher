import string

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

cipherShift = input("please enter the number of characters you wish to shift for this cipher: ")

while not cipherShift.isdigit():
    print("Invalid input.  Please enter a valid number.")
    cipherShift = input("please enter the number of characters you wish to shift for this cipher: ")

cipherShift = int(cipherShift)

phrase = input("Please enter the phrase you wish to encode: ")
cipherPhrase = ""

for char in phrase:
    if char == ' ':
        cipherPhrase += " "
    elif char.isdigit() or char in string.punctuation:
        cipherPhrase += char
    else:
        position = alphabet.index(char.lower())
        newPosition = (position + cipherShift) % 26
        
        if char.isupper():
            cipherPhrase += (alphabet[newPosition].upper()) 
        else: 
            cipherPhrase += (alphabet[newPosition])            
    # print(position)
    # print(alphabet[position])
    # print(newPosition)
    # print(alphabet[newPosition])

#print(cipherPhrase)
print(f'The phrase you input was: \"{phrase}\"')    
print(f'The phrase has been scambled to be: \"{cipherPhrase}\"')
