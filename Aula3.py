#Aula 3 do curso de Computacional Thinking
#1. Programa para leitura de nota

nota1 = float(input("O valor da nota 1"))
nota2 = float(input("O valor da nota 2"))
nota3 = float(input("O valor da nota 3"))

media_final = (nota1 + nota2 + nota3)/3 #variavel que define o valor da media para pesquisa da condição
print("A média do aluno é de:" , media_final)
if media_final >= 6:
    print("Aluno aprovado!")
elif (media_final >= 3) and (media_final < 5):
    print("Aluno em recuperação")
else:
    print("Aluno reprovado!")




#2. Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por km acima de 80km/h
velocidade = float(input("Qual a velocidade aferida?"))

if velocidade > 80:
    print("Calma la cidadão! Você foi multado")
    multa = (velocidade - 80) * 5 #multa dentro do if pois assim evitamos chamar processos desnecessarios
    print(f"O valor da multa é de R$ {multa:.2f} ")
else:
    print("Parabens! Sem multa pra você")

#3. Programa para ler 3 numeros e indicar maior e menor
valor1 = float(input("Insira o valor 1"))
valor2 = float(input("Insira o valor 2"))
valor3 = float(input("Insira o valor 3"))

maior = max(valor1, valor2, valor3) #dessa forma chamamos os valores com a função de maximo e minio
menor = min(valor1, valor2, valor3)

maior1 = valor1   #dessa maneira chamamos a função com a espinha logica para processamento independente
if valor2 > valor1 and valor2 > valor3:
    maior1 = valor2
elif valor3 > valor1 and valor3 > valor2: #elif funciona como uma pos negação para a condição exigida
    maior1 = valor3

menor1 = valor1
if valor2 > valor1 and valor2 > valor3:
    menor1 = valor2
elif valor3 > valor1 and valor3 > valor2:
    menor1 = valor3

print(maior1, menor1)

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")