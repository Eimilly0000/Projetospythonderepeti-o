#declarar

X: int = 0 
X1: int = 0 
X2: int = 0 
A: int = 0 
B: int = 0 
C: int = 0 
Delta: int = 0
import math  

#inicio

A = int (input("Digite o valor de A: "))
B = int (input("Digite o valor de B: "))
C = int (input("Digite o valor de C: "))
Delta = ((B*B) - 4*A*C)
if (Delta == 0) : 
 X = -B / (2*A)
 print ("Seu cálculo tem apenas uma raíz: ",X)
elif (Delta > 0) : 
 X1 = (-B + math.sqrt(Delta)) / 2 * A
 X2 = (-B - math.sqrt(Delta)) / 2 * A
 print ("Seu cálculo tem duas raízes: ", X1, "e" , X2)
else : 
 print ("Seu cálculo não tem raíz.")

#fim
