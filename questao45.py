#declarar

soma : int = 0
N : int = 0

#inicio

soma = 0 
N = 1

while (N <= 15): 
    if (N % 2 != 0 ):  
        soma = soma + (N / (N*N))
    else : 
     soma = soma - (N / (N * N))
    N = N + 1
    print ("O resultado da soma é: ", soma)
 
#fim