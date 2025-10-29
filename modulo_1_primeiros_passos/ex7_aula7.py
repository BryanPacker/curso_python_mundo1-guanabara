comp = float(input('Digite o comprimento: '))
larg = float(input('Digite a largura: '))
print('dado comprimento {} e largura {} a área da parede corresponde a {}m²\nconsiderando que 1 litro pinta 2m² será necessário {} litros de tinta'.format(comp, larg, comp*larg, (comp*larg)/2))