#declarar

VL1 : float = 0
VL2 : float = 0
Maior : float = 0

#inicio

VL1  = float(input("Digite um número: " ))
VL2 = float (input("Digite o segundo número: " ))
if (VL1 > VL2) :
 print (VL1,"é maior que ", VL2)
elif (VL1 == VL2) :
 print ("Digite números diferentes!")
else :
 print (VL2,"é maior que ", VL1)

#Fim