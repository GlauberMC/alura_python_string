
argumento = 'moedaorigem=real'
index = argumento.find('=')
substring = argumento[index + 1:]
print(substring)

listaargumentos = argumento.split('=')
print(listaargumentos)



'''
Vimos nessa aula que o método find ajuda a capturar valores de uma forma mais
dinâmica dentro de uma string qualquer. Analise o código abaixo:

celular = "(41)96574-1728"
indiceInicialCodigoArea = x
indiceFinalCodigoArea   = y

print (celular[indiceInicialCodigoArea:indiceFinalCodigoArea])

Com o objetivo de retirar o código de área sem os “()”, os valores de x e y 
podem ser substituídos por:


resposta: Termo x - celular.find(“(“) + 1 Termo y - celular.find(“)”)
'''

celular = "(41)96574-1728"
print(celular)

index = celular.find('(')
indiceInicialCodigoArea = celular[index + 1]
print(indiceInicialCodigoArea)

indiceFinalCodigoArea = celular[index + 2]
print(indiceFinalCodigoArea)
