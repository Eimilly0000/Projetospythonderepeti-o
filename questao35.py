#Declarar

N1 : int = 0
N2 : int = 0
Maior : int = 0
Menor : int = 0
Soma_Impar : int = 0
atual : int = 0
#inicio 
Maior = 0 
Menor = 0
N1 = int (input("Digite o primeiro valor: "))
N2 = int (input ("Digite o segundo valor: "))
Soma_Impar = 0 #soma dos ímpar tem que ser igual a zero
atual = Menor + 1 #atual é igual a menor mais um porque tem que fazer um loop

if (N1 > N2): #Vendo qual é o maior ou menor
    Maior = N1 
    Menor = N2
else:
    Maior = N2 
    Menor = N1
    atual = Menor + 1
while atual < Maior : 
    if (atual % 2 != 0) : #esse é o contador para que vá somando os ímpares e acumule no "soma_impar"
        Soma_Impar += atual #somar impar tem que somar igual ou ser que nem ele
    else: 
        print (".")

    atual += 1 #obrigatoriamente atual tem que somar 1
print (" A soma dos ímpares entre", Menor , "e", Maior, "é", Soma_Impar)


       


