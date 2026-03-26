#declarar

maior: int =0 
menor: int = 0
num : int = 0
i : int = 0

#inicio
num = int (input("Digite um número positivo: "))
maior = num 
menor = num
i = 2
while i <=100:
    num = int (input("Digite um número positivo: "))
    if (num > maior):
        maior = num
    elif (num < menor): 
        menor = num
    i = i + 1 
print ("Maior", maior)
print ("Menor", menor)

#fim