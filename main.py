from ExtratorArgumentosUrl import ExtratorArgumentosUrl

# url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar"
url = "moedaorigem=real&moedadestino=dolar"


argumentoUrl = ExtratorArgumentosUrl(url)
moedaOrigem, moedaDestino = argumentoUrl.extraiArgumentos()

print(moedaOrigem, moedaDestino)

