#declarar

base: int = 0
expoente : int = 0
resultado: int  = 0
cont : int = 0
#inicio

base = int (input("Digite o valor da base: "))
expoente = int (input("Digite o valor do expoente: "))

resultado = 1
cont = 0

while cont < expoente:
    resultado = resultado * base
    cont = cont + 1
print ("o resultado da potência é: ", resultado)

#fim