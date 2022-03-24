import pandas

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_df = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_df)
nato_dict = {row.letter: row.code for (index, row) in nato_df.iterrows()}

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def generate_phonetic():
    user_input = input("Enter a word: ")
    try:
        nato_list = [nato_dict[letter.capitalize()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters from the english alphabet please.")
        generate_phonetic()
    else:
        print(nato_list)

generate_phonetic()
