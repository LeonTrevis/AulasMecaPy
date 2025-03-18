# Aula2 do curso de python (eng. mecatronica 2025)

# 1.Saída de dados
print("Hello World!")

# 2. Exercicio solicitar o nome do usuario
print("Qual o seu nome?")
nome = str(input())
print("Seu nome é:", nome)

# 3. Exercicio solicitar numeros para somar, junto com o nome do usuario
print(nome, "escolha 3 valores a serem somados")
a1 = float(input())
b1 = float(input())
c1 = float(input())
soma = (a1+b1+c1)
print(nome, "a soma de", a1, b1, c1, "é de:", f"{soma:.2f}")

# 4. Exercicio de media + nome do usuario

print(nome, "entre com os valores das 3 notas")
a2 = float(input())
b2 = float(input())
c2 = float(input())
media = ((a2+b2+c2)/3)

print(nome, "a media das notas", a2, b2, c2, "é de:", f"{media:.2f}")

