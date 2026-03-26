#declarar

alt_ana : int = 0
alt_maria: int = 0
anos : int = 0

#inicio

anos = 0
alt_ana = 1.10
alt_maria = 1.50

while (alt_ana <= alt_maria):
    alt_ana = alt_ana + 0.03
    alt_maria = alt_maria + 0.02
    anos = anos + 1
print ("Serão necessários",anos,"anos para Maria ser maior que Ana")
print ("Altura final de Ana: ", alt_ana) 
print ("Altura final de Maria: ",alt_maria)

#fim
