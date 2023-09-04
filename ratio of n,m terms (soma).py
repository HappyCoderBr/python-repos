#   Faça um programa que mostre os n termos da Série a seguir:
#   S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
#   Imprima no final a soma da série.


i=1
j=1
soma=0
while i<100:
    print(f"{i}/{j}")
    razao=i/j
    i=i+1
    j=j+2
    soma=soma+razao
print(soma)
