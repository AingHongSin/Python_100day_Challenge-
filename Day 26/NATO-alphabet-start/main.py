import pandas


data = pandas.read_csv('nato_phonetic_alphabet.csv')
input_word = input("Enter a word: ").upper()

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

alpha_and_word_dist = {row.letter: row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
output_list = [alpha_and_word_dist[word] for word in input_word]

print(output_list)
