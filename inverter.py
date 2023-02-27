
string = input("Digite algo para ser invertido: ")

invertida = ""

for i in range(len(string)-1, -1, -1):
    invertida += string[i]

print(invertida)
