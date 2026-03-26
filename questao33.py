#declarar

N : int = 0
S : int = 0
D : int = 0

#inicio
D = 1 
S = 0
N = int (input("Digite um valor: "))

if(D > N): 
    print ("Número inválido!")
else: 
    while D <= N : #para que repta
        S = S + (1 / D)
        D = D + 1
    
print ("A série é: ", S) #print fora do while para mostrar o total
#fim
