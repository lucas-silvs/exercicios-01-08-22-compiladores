import re

with open ("Lucas da Silva Santos - ex03.c", "r") as file, open("ex03.out", "w+") as writefile:
    alfabeto = ["main" , "auto" , "break" , "case" , "char" , "const" , "continue" , "default" , "do" , "double" , "else" , 
    "enum" ,"extern" ,"float" ,"for" ,"goto" ,"if" ,"int" ,"long" ,"register" ,"return" ,"short" ,"signed" ,"sizeof" ,"static" , "struct", "switch", "typedef" , "union" , "unsigned" , "void" , "volatile" , "while"]

    for linhas in file:
        for i in range(len(alfabeto)):
            linhas = re.sub(r"\b" + alfabeto[i] + r"\b", alfabeto[i].upper(), linhas)
        writefile.write(linhas)
