valor_compra = float(input("Digite o valor da compra: R$ "))
valor_com_desconto = valor_compra - (valor_compra * 0.20)
valor_com_desconto2 = valor_compra - (valor_compra * 0.10)

if (valor_compra >= 1000):
    print("Você recebeu desconto!!", f"\nSubtotal: R${valor_compra}" f"\nTotal: R${valor_com_desconto}")

elif(valor_compra >=500):
     print("Você recebeu desconto!!", f"\nSubtotal: R${valor_compra}" f"\nTotal: R${valor_com_desconto2}")
else:
    print("Você não recebeu desconto!", f"\nSubtotal: R${valor_compra}" f"\nTotal: R${valor_compra}")