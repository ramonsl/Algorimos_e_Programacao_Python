#Crie um programa que solicite ao usuário uma frase e conte a quantidade de vogais presentes na frase.

frase=input("Digite a frase\n")
countConsoantes=0
countVogais=0
for ch in frase:
  if ch !='a' and ch != 'e' and ch !='i' and ch != 'o' and ch != 'u':
    countConsoantes=countConsoantes+1
    ##count+=
if ch =='a' or ch == 'e' or ch =='i' or ch == 'o' == ch == 'u':
    countVogais=countVogais+1
    ##count+=

print(f"A frase é {frase} e contem {countVogais} vogais e {countConsoantes} consoantes")
