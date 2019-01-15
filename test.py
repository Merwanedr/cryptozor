from cryptozor import Cryptozor

cryptozor = Cryptozor('usd', 'btc') # From USD to BTC

value = cryptozor.convert(8500) # Amount
print(value)