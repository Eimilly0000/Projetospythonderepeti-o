#declarar

venda :float = 0
preco_atual :float = 0
preco_novo : float = 0

#inicio

venda = float (input("Escreva o valor da venda: "))
preco_atual = float (input("Escreva o valor do preço atual: "))

if (venda < 500 and  preco_atual < 30000) : 
    preco_novo = preco_atual * 1.10 
    print ("O novo preço é de: ", preco_novo)
elif (venda >=500 and venda <1000) and (preco_atual >=30 and preco_atual < 80) :
    preco_novo = preco_atual * 1.15
    print ("O novo preço é de: ", preco_novo)
elif (venda>=1000 and preco_atual >= 80):
    preco_novo = preco_atual * 0.95
    print ("O novo preço é de: ", preco_novo)
else : #se cair aq é  pq nn deu certo em nenhuma acima
    preco_novo = preco_atual
    print ("Nenhuma condição atingida, preço mantido.")
#fim

