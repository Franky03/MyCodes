#Read names
with open("./Udemy/Mail+Merge+Project+Start/Input/Names/invited_names.txt") as names_file:
    names= names_file.readlines()

#See the names and replace  
with open("./Udemy/Mail+Merge+Project+Start/Input/Letters/starting_letter.txt") as letter_file:
    letter_contents= letter_file.read()
    for name in names:
        new_name= name.strip()
        new_letter=letter_contents.replace('[name]', new_name)
        print(new_letter)
        with open(f"./Udemy/Mail+Merge+Project+Start/Output/ReadyToSend/letter_for_{new_name}.txt", mode='w') as final_letter:
            final_letter.write(new_letter)
