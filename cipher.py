'''
Project: Caesar Cipher
Jared Joering
Code:You
October 28, 2024

Description: In this exercise we will implement a Caesar cipher with a 
right shift of 5. This exercise is based on the Caesar cipher exersise 
in the openSAP Python for Beginners course. If you have already solved 
it as part of the Learn Python course you can re-use your code here.

Write a Python program that encrypts text given by the user. The program
should ask the user for a plain text sentence and print the encrypted
text. The text should be encrypted using a caesar cipher with a right 
shift of 5.
'''

prompt = input("Please enter a sentence: ")
new_sentence = []

for letter in prompt:
    if letter.isalpha():    # Checking to see if the letter is alphabetical
        new_sentence.append(chr(ord(letter) + 5)) # Moving letter five to the 'right'
    else:
        new_sentence.append(letter)   # Else I'm just appending whatever that current letter is

print("The encrypted sentence is:", ''.join(new_sentence))
