#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
name1 = input('Primeiro aluno: ')
name2 = input('Segundo aluno: ')
name3 = input('Terceiro aluno: ')
name4 = input('Quarto aluno: ')
lista = [name1, name2, name3, name4]
shuffle(lista)
print('A ordem de apresentação será\n{}'.format(lista))
