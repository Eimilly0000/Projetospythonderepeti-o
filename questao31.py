#declarar
A: int = 0
N: int = 0

#inicio
N = float(input("Digite um número: "))
if (N >= 10 and N<=150):
    A = N*N
    print("O quadrado de",N, "é:",A)
else: 
    print("Aceito só números >=10 e <=150!")

#Fim
 