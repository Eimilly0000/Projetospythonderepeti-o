#declarar
N1: int = 0
N2: int = 0
num : int = 0
i : int = 0
primo : int = 0
aux: int = 0
#inicio

N1 = int (input("Digite o primeiro número: "))
N2 = int (input("Digite o segundo número: "))

if (N1 > N2):
    aux = N1
    N1 = N2 
    N2 = aux 
num = N1
print ("N1: ", N1)
print ("N2: ", N2)
print ("Num: ", num)
print ("N2: ", N2)
while num <= N2 :
    primo =0 
    i = 1

    while i <= num : 
     if (num %i == 0): 
        primo = primo + 1
    i = i + 1
    print (i)

    if (primo ==2):
        print (num)  
    
    num = num + 1
    print ("Entrou no while")


#fim