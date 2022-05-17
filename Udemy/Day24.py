#modo padrão é 'r' de read
with open("./Udemy/day24doc.txt", mode='r') as file:
    contents= file.read()
    print(contents)
    # file.close() com o with não precisa dar close


#modo 'a' é de append que acrescenta algo no arquivo

with open("./Udemy/day24doc.txt", mode='a') as file:
    file.write('\nHello Other Universe from the World')

#modo 'w' é para escrever algo em um arquivo, mas se tiver algo no arquivo vai substituir o que tem nele
#é bom para quando for criar um novo arquivo, ex

# with open("./Udemy/new_doc.txt", mode='w') as file:
#     file.write("New exemplo para a aula")

    

