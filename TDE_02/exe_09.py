print('9. F.U.A para calcular o valor de lucro que um vendedor tem em um produto, com base em seu preço de custo e o preço de venda.')
preco_custo= float(input('Digite o preço do produto: R$'))
preco_venda= float(input('Digite o valor da venda: R$'))
lucro= preco_venda - preco_custo
print(f'Com base no valor do custo de {preco_custo} e o valor da venda de {preco_venda}, seu lucro é de: R${lucro}')