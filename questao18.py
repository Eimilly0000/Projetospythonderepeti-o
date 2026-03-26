#declarar
V1 : int = 0
V2 : int = 0 
RST : int = 0

#inicio

V1 = int(input("Digite o 1° número: " ) )
V2 = int (input("Digite o 2° número: " ) )
  
if (V1 > V2) :
 RST = V1 - V2
 print ("A Diferença é de : ", RST)
else:
 RST = V2 - V1
 print ("A Diferença é de : ", RST)

#Fim