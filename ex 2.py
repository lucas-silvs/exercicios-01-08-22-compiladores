

from operator import le


with open ("teste2.c", "r") as file:
    numeros = []
    alfabeto = ["asm" , "auto" , "break" , "case" , "char" , "const" , "continue" , "default" , "do" , "double" , "else" , 
    "enum" ,"extern" ,"float" ,"for" ,"goto" ,"if" ,"int" ,"long" ,"register" ,"return" ,"short" ,"signed" ,"sizeof" ,"static" , "struct", "switch", "typedef" , "union" , "unsigned" , "void" , "volatile" , "while"]

    count = [0 for i in range(len(alfabeto))] 
    
    

    for linhas in file:
        print("linha: "+ linhas)
        for i in range(len(alfabeto)):
            count[i] = count[i] + linhas.count(alfabeto[i])

for i in range(len(alfabeto)):
    print( alfabeto[i] + " : " + str(count[i]))

