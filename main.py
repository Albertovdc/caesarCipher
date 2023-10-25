alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(t, s):
    # encrypt = []
    cipher_text = ""
    # Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and
    # print the encrypted text.
    for letter in t:
        number = alphabet.index(letter) + s
        cipher_text += alphabet[number]

    print(cipher_text)


# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
def decrypt(textEncrypt, shiftE):
    textOriginal = ""
    # Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
    for n in textEncrypt:
        number = alphabet.index(n) - shiftE
        textOriginal += alphabet[number]

    print(textOriginal)


# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. The call the
# correct function based on that 'direction' variable. You should be able to test the code to encrypt *AND* decrypt a
# message.

if direction.lower() == "encrypt":
    encrypt(text, shift)
elif direction.lower() == "decrypt":
    decrypt(text, shift)
else:
    print("You don't chose a option")
