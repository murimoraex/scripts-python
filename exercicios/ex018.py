#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo. Dica: Biblioteca de ângulos

import math
ang = int(input('Digite o ângulo que você deseja: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem a COSENO de {:.2f}'.format(ang, cos))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tan))
