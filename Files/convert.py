#pip install image-to-ascii-pyaoponto
from image_to_ascii import ImageToAscii
obj= ImageToAscii()
#Endereço da imagem
obj.image_path("luffy.png")
#Imprime na tela
obj.plot()
#Salvar como arquivo txt
obj.save_to_file()