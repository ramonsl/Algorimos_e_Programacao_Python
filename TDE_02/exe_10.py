print('10.F.U.A que leia o preço de um produto e a quantidade comprada e exiba para o usuário o preço que ele tem que pagar pela compra.')
preco= float(input('Digite o preco do produto: R$'))
quantidade= float(input('Digite a quantidade de produtos comprados:'))
calculo= preco * quantidade
print(f'O preco total vai ser de: R${calculo}')