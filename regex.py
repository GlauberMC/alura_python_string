import re

email1 = 'Meu número é 1234-1234'
email2 = 'Fale comigo em 1234-1234 esse é o meu telefone'
email3 = '1234-1234 é o meu celular'
email4 = 'nxlendkwndwe 99534-2390 dwoudbwoedbw 1234-1234 e 12345678'

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

# retorno  = re.search(padrao,email4)
# print(retorno.group())

retorno = re.findall(padrao, email1)
print(retorno)

