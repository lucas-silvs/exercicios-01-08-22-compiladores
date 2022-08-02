

from operator import le


with open ("teste.c", "r") as file:
    numeros = []
    alfabeto = ["a" , "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" ,"m" ,"n" ,"o" ,"p" ,"q" ,"r" ,"s" ,"t" ,"u" ,"v" ,"w" ,"x" ,"y" , "z", "1", "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0", " "]

    count = [0 for i in range(len(alfabeto))] 
    
    

    for linhas in file:
        print("linha: "+ linhas)
        for i in range(len(alfabeto)):
            count[i] = count[i] + linhas.count(alfabeto[i])

for i in range(len(alfabeto)):
    print( alfabeto[i] + " : " + str(count[i]))
