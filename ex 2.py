

from operator import le


with open ("teste2.c", "r") as file, open("teste2-maiusculo.c", "w+") as writefile:
    alfabeto = ["main" , "auto" , "break" , "case" , "char" , "const" , "continue" , "default" , "do" , "double" , "else" , 
    "enum" ,"extern" ,"float" ,"for" ,"goto" ,"if" ,"int" ,"long" ,"register" ,"return" ,"short" ,"signed" ,"sizeof" ,"static" , "struct", "switch", "typedef" , "union" , "unsigned" , "void" , "volatile" , "while"]
 
    for linhas in file:
        for i in range(len(alfabeto)):
            linhas = linhas.replace(alfabeto[i], alfabeto[i].upper())
        writefile.write(linhas)



