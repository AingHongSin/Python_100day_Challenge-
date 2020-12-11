alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

def ceasar(text, shift, direction):
    letter = ""
    for letter in text:
        position = alphabet.index(letter)
        if direction == "decode":
            shift *= -1
        new_position = position + shift
        letter += alphabet[new_position]
    print(f"Here's the {direction}d text is {letter}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
ceasar(text, shift, direction)