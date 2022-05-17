from resources import logo
print(logo)
print("Welcome to the secret auction program.")
people={}
def highest(dic):
    maior=0
    namai=''
    for k, v in dic.items():
        if v>maior:
            maior= v
            namai=k
    print(f"The winner is {namai} with a bid of ${maior}.")

while True:
    name= str(input("What is your name?: ")).strip()
    bid= int(input("What's your bid?: $"))
    people[name]= bid
    while True:
        resp= str(input("Are there any other bidders? Type 'yes' or 'no': ")).lower().strip()
        if resp=='yes' or resp=='no':
            break
        else:
            print("ERROR")
    if resp=='no':
        break
highest(people)
