#declarar
d1 : int = 0
d2 : int = 0

#inicio
d1 = 1

while d1 <= 6 : 
    d2 = 1
    while d2 <= 6: 
        if (d1 + d2 == 7):
            print (d1, "+",d2, "=7")
        d2 = d2 + 1
    d1 = d1 + 1    