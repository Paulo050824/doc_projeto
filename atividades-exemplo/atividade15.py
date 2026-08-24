valor_compra = float(input("Digite o valor da compra: R$ "))
valor_com_desconto = valor_compra - (valor_compra * 0.10)

if (valor_compra >= 200):
    print("Você recebeu desconto!!", f"\nSubtotal: R${valor_compra}" f"\nTotal: R${valor_com_desconto}")
else:
    print("Você não recebeu desconto!", f"\nSubtotal: R${valor_compra}" f"\nTotal: R${valor_compra}")