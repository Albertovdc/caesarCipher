alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def cesar(directionUser, userText, shiftAmount):
    text = ""
    if directionUser == "decode":
        shiftAmount *= -1
    for letter in userText:
        if letter in alphabet:
            number = alphabet.index(letter) + shiftAmount
            text += alphabet[number]
        elif letter == " ":
            text += " "
        else:
            text += letter
    print(text)
    answer = input("Do you want to restart the cipher program? (type 'yes' or 'no')").lower()
    if answer == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        cesar(direction, text, shift)
    else:
        print("See you :D")

shift = shift % 26

cesar(direction, text, shift)
