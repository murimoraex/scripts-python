#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre sua média. Dica: Testar, Ordem de Precedência.

n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('Segunda nota do aluno: '))
print('A média entre {} e {} é igual a {:.1f}'.format(n1, n2, (n1 + n2)/2))
