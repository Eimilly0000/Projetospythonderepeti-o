#declarar

N: int = 0
S: int = 0
F: int = 0
D: int = 0

#inicio
N = int (input("Digite o número: "))
S = 1 
D = 1
F = 1

while D<=N : #para que repita
    F = F * D #fatorial
    S = S + (1/F) #a soma
    D = D + 1 #a soma para que se repita
print("A soma é: ", S)


#fim