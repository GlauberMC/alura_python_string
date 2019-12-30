class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url
        else:
            raise LookupError('URL inválida!!!!')

    @staticmethod
    def urlEhValida(url):
        if url:
            return True
        else:
            return False

    def extraiArgumentos(self):

        # url = "moedaorigem=real&moedadestino=dolar"
        #
        # index = url.find("moedadestino") + len("moedadestino") + 1
        # substring = url[index:]
        # print(substring)

        buscaMoedaOrigem  = "moedaorigem"
        buscaMoedaDestino = "moedadestino"

        indiceInicialMoedaDestino   = self.econtraIndiceInicial(buscaMoedaDestino)

        indiceInicialMoedaOrigem    = self.econtraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaOrigem      = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem, moedaDestino

    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada) +1