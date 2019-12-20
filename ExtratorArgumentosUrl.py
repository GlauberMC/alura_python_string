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


        indiceInicialMoedaDestino   = self.url.find('=', 15) + 1

        indiceInicialMoedaOrigem    = self.url.find('=') + 1
        indiceFinalMoedaOrigem      = self.url.find("&")

        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaOrigem]

        moedaDestino = self.url[indiceInicialMoedaDestino:]

        return moedaOrigem, moedaDestino