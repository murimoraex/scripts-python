#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, escrevendo o nome do escolhido.

import random 
first = input('Primeiro aluno: ')
secon = input('Segundo aluno: ')
third = input('Terceiro aluno: ')
forth = input('Quarto aluno: ')
lista = [first, secon, third, forth]
rand = random.choice(lista)
print('O aluno escolhido foi {}'.format(rand))
