 
cigarrosPorDias=int (input("Digite quantos cigarros voce consome por dia? "))
fumante_tempo=int(input("A quantos meses voce fuma? "))
tempo_vida= (cigarrosPorDias * fumante_tempo) * 15
 
 
if fumante_tempo <= 3 :
    print(f"Voce tera dentes amarelos")
 
if fumante_tempo >3 and fumante_tempo <= 12 :
    print(f"Voce tera perda de paladar e respiração comprometida")
 
if fumante_tempo > 13 :
    print(f"Voce tera pulmao comprometido")
 
print(f"Voce perder {tempo_vida} minutos de vida. ")