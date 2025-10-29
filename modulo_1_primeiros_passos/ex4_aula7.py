from operator import is_not

n = int(input('Digite um valor inteiro em centímetros: '))
print('O valor em centímetros é {:.2f}, em Metros {:.2f} e milimetros {:.2f}'.format(n, n/100, n*10))