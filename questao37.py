#declarar
N : int = 0
A : int = 0
B: int = 0
P : int = 0

#inicio
N = int (input("Digite N: "))

A = 0
B = 1
contador = 1


while (contador  < N): #while é usado em repetição
    P = A + B
    A = B
    B = P
    contador = contador + 1
if (B <= 90): 
        print (B, " chegou no seu n'ésimo termo")
else :
        print (B, "é grande")     

#fim