#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
á = l * a
t = á/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²\nPara pintar essa parede, você precisará de {}l de tinta.'.format(l, a, á, t))
