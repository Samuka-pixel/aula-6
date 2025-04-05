name = str(input("Qual é o nome do seu ficheiro?: "))
file = open(f'{name}.txt', "r")
print(file.read())
print()