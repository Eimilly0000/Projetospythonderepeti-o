#declarar

N1: float = 0
N2: float = 0
N3: float = 0
N4: float = 0
Media : float = 0

#inicio

N1 = float (input("Digite a 1° nota: "))
N2 = float (input ("Digite a 2° nota: "))
N3 = float (input ("Digite a 3° nota: "))
N4 = float (input ("Digite a 4° nota: "))
Media = (N1 + N2 + N3 + N4)/4
if (Media >= 6): 
    print ("Aprovado!")
elif (Media >= 3 and Media <6):
    print ("Exame!")
else:
    print ("Retido!")

#Fim    