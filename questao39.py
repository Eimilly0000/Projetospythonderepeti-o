#declarar

graos : int = 0
total :int = 0
casa : int = 1

#inicio

while casa <= 64 : 
    total = total + graos
    graos = graos * 2
    casa = casa * 1 
print ("Total de grãos", total)

#fim