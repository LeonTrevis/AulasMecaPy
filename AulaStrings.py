frase="Hello World!"
print(len(frase))
print(frase[-2])

#concatenação é a soma de duas ou mais strings
#formas de concatenar:
a="Hello"
b="World"
print(a, b)
print(a + " " + b)
c="!"
print (a, b + c*3)

#concatenação de strings com numeros
d="53"
e="10"
f="5"
print(d+e+f+c*3)

#reposicionamento de caracteres
# cep = input("CEP: ")
# print(f"CEP: {cep[:5]}-{cep[5:]}")

#strings são imutáveis, para alterá-las precisamos transformar em lista
frase=list("Hello World!")
print(frase)
frase[11]="!!!"
print(frase)

#join retorna a lista para string, as "" com espaço espaçam as letras na frase
frase=" ".join(frase)
print(frase)

#funçes starswith e endswith fazem uma varredura para buscar correspondencia nos dados
frase="Hello world!"
print(frase.startswith("Hello"))
print(frase.endswith("world"))
#world não é reconhecido pelo endswith pq não tem o ! no final

print(frase.count("o"))
print(frase.find("hello"))

#funções que alteram a string
titulo="Hello World!"
print(titulo.center(126, "_"))
print(titulo.ljust(50,"."))
print(titulo.rjust(50,"."))
print(titulo.split())
titulo_Trad = titulo.replace("Hello World", "Olá Mundo") #muda momentaneamente o valor de texto que estava alocado, sem alterar a variavel
print(titulo)
print(titulo_Trad)

print("Hello", "World", sep='.')#separadores são espaço por definição, mas podemos alterar as interações com a função sep
print("Hello", "World", end="\nTchau")#muda a forma como finalizamos uma concatenação, \n pula uma linha no fim do mesmo print
