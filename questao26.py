#declarar 

N1 : int = 0
N2 : int = 0

#inicio

N1 = int (input("Digite o primeiro valor: "))
N2 = int (input("Digite o segundo valor: "))

if(N1 > N2): 
   if (N1 % N2 ==0):
    print (N1 , "é multíplo de", N2)
   else: 
      print (N1 , "não é multíplo de", N2)
else : #N2 > N1
    if (N2 % N1 ==0): 
     print (N2, "é multíplo de",N1)
    else :
     print (N2, "não é multíplo de", N1)

#fim