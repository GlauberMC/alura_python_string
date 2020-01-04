from ExtratorArgumentosUrl import ExtratorArgumentosUrl


url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"
# url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar"
# url = "https://www.bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar"
# url = "moedaorigem=real&moedadestino=dolar"

argumentoUrl = ExtratorArgumentosUrl(url)
moedaOrigem , moedaDestino = argumentoUrl.extraiArgumentos()
valor = argumentoUrl.extraiValor()

print(moedaOrigem)
print(moedaDestino)
print(valor)
print(argumentoUrl)


# index = url.find('moedadestino') + len('moedadestino') + 1
# substring = url[index:]
# print(substring)