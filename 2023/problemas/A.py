"""
Altura Mínima

Carlitos é um entusiasta de aventuras com um amor insaciável por parques de diversões. 
Apesar de sua paixão vibrante, Carlitos enfrenta um desafio único: sua estatura limitada. 
Enquanto planeja ansiosamente sua aventura de fim de semana, ele percebe que suas limitações de altura 
podem atrapalhar sua experiência no parque de diversões. 
Não se trata apenas de escolher um parque; trata-se de encontrar um onde ele possa aproveitar a emoção dos brinquedos.

Imagine o caleidoscópio de cores, as risadas jubilosas e a adrenalina dos passeios. 
Carlitos sempre foi atraído pela energia dos parques de diversões. 
Com o fim de semana se aproximando, ele se debruça sobre os folhetos do parque, estudando os requisitos de 
altura de cada brinquedo. Seu objetivo é maximizar sua diversão, e é aí que você entra.

Sua tarefa é ajudar Carlitos a determinar o número de brinquedos que ele pode desfrutar em um parque 
específico. Considerando sua altura e os requisitos mínimos de altura de cada brinquedo, oriente-o a 
aproveitar ao máximo sua aventura no parque de diversões.

Entrada
A primeira linha contém dois números inteiros, N e H (1 ≤ N ≤ 6 e 90 ≤ H ≤ 200), que representam a 
quantidade de brinquedos em um parque e a altura de Carlitos em centímetros, respectivamente. 
Na segunda linha da entrada, serão fornecidas as alturas mínimas A1,…,AN (90 ≤ Ai ≤ 200) 
de cada um dos brinquedos do parque.

Saída
Seu programa deve imprimir uma única linha contendo a quantidade de brinquedos nos quais
Carlitos pode ir, ou seja, a quantidade de brinquedos para os quais a altura de Carlitos é 
pelo menos tão grande quanto a altura mínima necessária.
"""

n, h = map(int, input().split())
A = list(map(int, input().split()))

res = len([a for a in A if a <= h])

print(res)