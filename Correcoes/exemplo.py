

from turtle import right


frutas = ["maça","abacaxi","uva","limão"]


for fruta in frutas:
    if fruta=="melão":
        print("Oba tem melão!")
        break
    else:
        print("Não é melao")
else:
    print ("Não tem melão")


#print (frutas[2])
x=0
#for x in range(2):
 #   print(frutas[x]) 

for qualquercoisa in frutas:
    print(qualquercoisa)

for i,fruit in enumerate(frutas):
    print(i,fruit)

vezes=0
while vezes<10: 
    print(f"{vezes}Vou me comportar !!!")
    if vezes==4:
        break
    if vezes==5:
        continue
    vezes+=1  #vezes=vezes+1



while True:
    senha=input ("Digite sua senha!")
    if senha=="123456":
        print("Acesso liberado!")
        break
    else:
        print("Senha invalida!")

print(f"Final do laço {vezes}")


vezes=0
for vezes in range(10):
    print(f"{vezes+1}Vou me comportar !!!")

for vezes in range(2,20,3):
    print(f"{vezes+1}Vou me comportar !!!")

for vezes in [1,2,3,4,5,6]:
    print(f"{vezes+1}Vou me comportar !!!")