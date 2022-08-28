import os


with open ("Lucas da Silva Santos - ex03.c", "r") as file:
    contador = {"espaço": 0 , "tab": 0, "quebra de linha": 0}
    numLinhas = 0
    for linhas in file:
        numLinhas+=1
        for char in linhas:
            if(char == "\t"):
                contador["tab"] += 1
            elif(char == " "):
                contador["espaço"] += 1
            elif(char == "\n"):
                contador["quebra de linha"] += 1
            elif (char not in contador.keys() and char!="\t" and char!= " " and char!="\n"):
                contador[char] = 1
            else:
                contador[char] += 1

print("Tamanho do arquivo lido: " + str( os.stat("Lucas da Silva Santos - ex03.c").st_size) + " bytes")
print("Número de linhas do arquivo lido: " + str(numLinhas))

for char in sorted(contador, key=lambda item:contador[item]):
    print(f'{char}: {contador[char]}')