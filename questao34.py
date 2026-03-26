#declarar

N : float = 0
M : float = 0 
A : float = 0

#inicio

N = int (input("Digite um número: "))
A = 1
if (N < 0 or N > 10): 
 print ("Número inválido!")
else: 
    while A <= 10: 
     M = N * A
     print(N, "x", A , "=", M) 
     A = A + 1
     
#fim       
    
  