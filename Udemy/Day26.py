numbers= [1,2,3]
new_list=[n+1 for n in numbers]
print(new_list)

name= 'kAIky'
letters_list= [letter for letter in name]
print(letters_list)

new_range= [r*2 for r in range(1,5)]
print(new_range)

#Conditional LC
# new_list= [ne_item for item in list if test]
names=['Alex', 'Beth','Caroline', 'Eleanor', 'Dave', 'Freddie']
short_name= [name for name in names if len(name)<5]
upper_name= [name.upper() for name in names if len(name)>=5]
print(short_name)
print(upper_name)
