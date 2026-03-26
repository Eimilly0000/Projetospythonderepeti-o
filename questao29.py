#declarar

poupanca : float = 0
renda_fixa : float =0 
valor : float = 0
resultado : float = 0
tipo : float = 0
#inicio
valor = float (input("Digite o valor do investmento: "))
tipo = float (input("Digite o tipo de investimento, (1 = Poupança, 2 = Renda Fixa): "))

if (tipo==1): 
    resultado = valor * 1.03 # 3% de correção
    print ("Em trinta dias na poupança será: ",resultado)
elif (tipo==2): 
    resultado = valor * 1.05 # 5% de correção
    print ("Em trinta dias seu valor na renda fixa será: ",resultado)
else: 
    print ("Investimento inválido!")
#fim