#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import sqrt, hypot
cato = float(input('Comprimento do cateto oposto: '))
cata = float(input('Comprimento do cateto adjacente: '))
hipo = sqrt(cato**2+cata**2)
h = hypot(cato, cata)
print('A hipotenusa vai medir {:.2f}'.format(hipo))
