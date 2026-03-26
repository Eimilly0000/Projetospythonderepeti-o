#declarar
v1 : int = 0
v2 : int = 0

#inicio

v1 = int (input("Digite o 1° número: "))
v2 = int (input("Digite o 2° número: "))
if (v1 == v2): 
   print ("Digite números diferentes!")

elif (v1 > v2): 
   print (v1, "e" , v2)

else : 
   print (v2 , "e", v1)

#fim
