#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar. Considere: US$1,00 = R$3.27

din = float(input('Quanto dinheiro você tem na carteira? R$'))
dol17 = din / 3.27
dol24 = din / 5.62
print('Com R${} você poderia comprar, em 2017, US${:.2f}.\nHoje você compra US${:.2f}.'.format(din, dol17, dol24))
