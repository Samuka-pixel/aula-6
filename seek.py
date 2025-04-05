name = str(input("Qual é o nome do seu ficheiro?: "))
file = open(f'{name}.txt', "r",encoding="utf8")
file.seek(28)
print(file.readline())