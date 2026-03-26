#declarar: 

num : int = 0
soma : int =0 
denominador: int = 0

#inicio

num = 1
denominador = 1
soma = 0

while num <= 50: 
    soma = soma + (num / denominador)
    num = num + 1
    denominador = denominador + 2
print ("O resultado da soma é: ", soma)

#fim