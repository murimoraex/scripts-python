#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela sua porção inteira. Ex: Digite um número: 6.127 O número 6.127 tem a parte inteira 6. Dica: Funções classes modulo math

from math import floor
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, floor(num)))
