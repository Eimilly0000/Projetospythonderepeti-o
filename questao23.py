#Declarar

V1: int = 0
V2: int = 0
V3: int = 0
V4: int = 0
A: int = 0

#inicio
V1 = int (input("Digite o 1° Valor: "))
V2 = int (input("Digite o 2° Valor: ")) 
V3 = int (input("Digite o 3° Valor: "))
V4= int (input("Digite o 4° Valor: "))

if (V1 < V2 < V3):

   if (V4 > V3 ):
      print("Sua ordem é: ", V1 , V2 , V3, V4)
    
   else : 
      print ("Sua ordem é: ", V4 , V1 , V2 , V3 )     
else:
   A = int (input("Os valores 1, 2 e 3 devem estar em ordem crescente!!(aperte Enter)"))
#Fim