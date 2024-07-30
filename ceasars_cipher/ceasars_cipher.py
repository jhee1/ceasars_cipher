alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
,'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
from ceasar_art import art
print(art)
condition = True
while condition:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    shift = shift % 26
    def ceasar(start_text, shift_amount, cipher_direction):
        end_text = ""
        if cipher_direction == "decode":
            shift_amount *= -1
            
        for char in start_text:
            if char in alphabet:   
                position = alphabet.index(char)
                new_position = position + shift_amount
                end_text += alphabet[new_position]
            else:
                end_text += char
        print(f"The {cipher_direction}d text is {end_text}")

    ceasar(start_text=text, shift_amount=shift, cipher_direction=direction)
    asking_user = input("Do you want to continue? Type 'yes' or 'no':\n")
    if asking_user == 'no':
        print("Goobye soldier!")
        condition = False

