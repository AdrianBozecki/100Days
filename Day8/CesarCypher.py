alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift_amount, mode):
    modified_text = ""

    if mode == 'decode':
        shift_amount *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            if new_position > len(alphabet) - 1:
                new_position -= len(alphabet)

            new_letter = alphabet[new_position]
            modified_text += new_letter
        else:
            modified_text += letter

    print(f"The encoded text is {modified_text}")


while True:
    mode = input("Do you want to encode, decode or exit?\n")
    if mode == 'exit':
        break

    shift = int(input('How many letters do you want to shift?\n'))
    shift = shift % len(alphabet)

    message = list(input('Type a message you want to encode/decode:\n').lower())

    caesar(message, shift, mode)