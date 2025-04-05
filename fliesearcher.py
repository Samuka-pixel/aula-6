name = str(input("Qual é o nome do seu ficheiro?: "))
file = open(f'{name}.txt', "w")
frase = str(input("O que deseja escrever?"))
file.write(frase)