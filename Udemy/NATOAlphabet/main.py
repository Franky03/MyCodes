import pandas as pd
#TODO 1. Create a dictionary in this format: {"A": "Alfa", "B": "Bravo"}
data= pd.read_csv('./Udemy/NATOAlphabet/nato_alph.csv')
alphabet_dict= {row.letter: row.code for (index, row) in data.iterrows()}
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate():
    word= str(input('Enter a word: ')).upper()
    try:
        letters= [l for l in word]
        phon_code= [alphabet_dict[letter] for letter in letters]
        print(phon_code)
    except:
        print("Sorry, only letters on alphabet.")
        generate()

generate()
