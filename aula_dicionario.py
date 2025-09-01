# #Codigo exemplo da aula de dicionario
# rm_alunos = {"563469": ["Giovanna", "2007"], "562227": ["Allana", "2004"]}
# print(rm_alunos)
# print(rm_alunos["563469"])
# print(rm_alunos["562227"])
# #.copy faz uma copia exata da lista, sem que ela se altere ao longo do codigo (backup)
# rm_alunos_back=rm_alunos.copy()
#
# #apaga a chave da gi do dicionario
# del rm_alunos["563469"]
# print(rm_alunos)
# print(rm_alunos_back)
#
# #modifica o indice 1 (ano de nascimento) na chave da allana
# rm_alunos["562227"][1]="2003"
# print(rm_alunos)
#
# #mostra se a chave esta relacionada ao dicionario
# print("562227" in rm_alunos)
# print("563469" in rm_alunos)
#
# #funções que apresentam a chave endereçada e os valores nela relacionados
# print(rm_alunos.keys())
# print(rm_alunos.values())


# #Dicionario para enderçar preço a produtos
# tabela = {"alface": 1.9, "batata": 15, "tomate": 8.5, "feijão": 3.5}
# while True:
#     #.lower() transforma o input em minusculo, as chaves devem estar em minusculo, .captalize() e . upper() também funcionam, mas deve bater as informações das chaves
#     produto = input ("Digite o nome do produto ou fim para terminar: ").lower()
#     if produto == "fim":
#         break
#     if produto in tabela:
#         print(f"Preço: R${tabela[produto]:.2f}")
#     else:
#         print("Produto não encontrado")

# #Dicionario para cursos da FIAP
# cursos_pre = {"data science": ["2.285,00", "2 anos"], "engenharia mecatrônica": ["2.485,00", "5 anos"], "segurança cibernética": ["2.635,00", "2 anos"]}
# while True:
#     curso = input("Entre com o curso a pesquisar e fim para sair: ").lower()
#     if curso == "fim":
#         break
#     if curso in cursos_pre:
#         print(f"Mensalidade: {cursos_pre[curso][0]}")
#         print(f"Duração: {cursos_pre[curso][1]}")
#     else:
#         print("Curso não encontrado")