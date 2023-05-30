
#5. Faça um programa que receba o valor de um carro e mostre uma tabela com os seguintes dados: preço final, quantidade de parcelas e valor da parcela. Considere o seguinte:
#A)  o preço final para compra à vista tem desconto de 20%:
#B)  a quantidade de parcelas pode ser: 6, 12, 18, 24, 30, 36, 42, 48, 54 e 60;
#C) os percentuais de acréscimo encontram-se na tabela a seguir.

#ler preco
#mostrar preco final
#mostrar quatidade de pacerlas e valolre

valor_do_carro=float(input("Digite o valor do carro: "))
valor_a_vista=valor_do_carro*0.8
print(f"O valor a vista é {valor_a_vista}")
juros=0.03
parcelas=6
for i in range(10):
    valor_em_parcelamento=valor_do_carro*(1+juros)
    print(f"O valor em {parcelas} vezes é {valor_em_parcelamento} - juros = {juros}")
    parcelas+=6
    juros+=0.03



#valor=valor*3/100
