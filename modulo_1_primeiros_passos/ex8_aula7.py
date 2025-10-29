n = float(input('Qual o valor do item?'))
d = float(input('Qual o desconto?(Não use % e use padrão internacional x.xx)'))
print ('dado valor {} e desconto {} o valor final fica {}'.format(n, d, n - ((n*d)/100)))