#declarar

F : int =0
N : int = 0 

#inicio
N = int(input("Digite um número: "))
F = 1
if (N<0):
   print("Número inválido!")
     
else: 
     while N > 1: #pra repetir 
      F = F * N
      N = N - 1
      print ("O fatorial é", F)    

#fim