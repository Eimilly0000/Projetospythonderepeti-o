#declarar

H: int = 0
M: int = 0
D: int = 0
HI: int = 0
MI: int = 0
HF: int = 0
MF: int = 0
TI : int = 0
TF: int  = 0
#inicio

HI = int (input("Digite a hora inicial (Apenas a hora, ex:1): "))
MI = int (input("Digite o minuto(EX:30): "))
HF = int (input("Digite a hora final (Apenas a hora): "))
MF = int (input ("Digite o minuto final(Apenas o minuto): "))

TI = (HI * 60 + MI) #tempo inicial recebe hora inicial vezes 60min mais minuto inicial
TF = (HF * 60 + MF) # tempo final recebe a hora final vezes 60min mais o minuto final
D = (TF - TI) # dias recebe tempo final menos tempo inicial (pra saber se virou o dia)

if (D <= 0): # se virou o dia
    D = D + 1440
    H = D // 60 #duas barras garantem que o numero seja inteiro
    M = D % 60
    print ("O jogo teve a duração de ", H, "horas e", M , "minutos")
else : #senão
    H = D / 60
    M = D % 60
    print ("O jogo teve a duração de ", H, "horas e", M , "minutos")

#fim