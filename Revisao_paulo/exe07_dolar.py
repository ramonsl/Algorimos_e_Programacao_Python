#Desenvolva um programa que converta um valor em dólar para real e real para dólar O
# usuário deve informar a quantidade de dólares e a taxa de câmbio atual. O programa deve calcular e exibir 
# o valor equivalente em reais. Utilize um menu para escolher a saída.

while True:
  
  opcao=int(input("1 para Dol-> Reais \n2- Para Real -> Dol\n"))
  cotacao_dolar=float(input("Digite a cotaçao do Doleta"))
  valor_a_ser_convertido= float(input("Qual o valor?\n"))
  if opcao ==1:
    valor_convertion=valor_a_ser_convertido*cotacao_dolar
    print(f" O Valor {valor_a_ser_convertido} em reais é R${valor_convertion}")
  elif opcao ==2:
    valor_convertion= valor_a_ser_convertido/cotacao_dolar
    print(f" O Valor {valor_a_ser_convertido} em dolars é ${valor_convertion}")
  else:
    print("Opção invalida")
