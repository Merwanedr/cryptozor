# Cryptozor.py

## A Python Cryptocurrency converter.

### Installing:
``` bash
# install using pip
pip3 install cryptozor.py
```

### Example:
``` python
from cryptozor import Cryptozor

# From USD to BTC
cryptozor = Cryptozor('usd', 'btc')

# Amount
value = cryptozor.convert(8500)

# Float value
print(value) 
```

### Currency support: 

Cryptocurrencies:
* Bitcoin (BTC)
* Ethereum (ETH)
* Ethereum Classic (ETC)
* Bitcoin Cash (BCH)
* Litecoin (LTC)
* ZCash (ZEC)
* 0x (ZRX)

Fiat currencies:
* Every fiat currency on earth (I guess)

### Donate:

Yeah I know I don't really deserve a donation for this tiny thing but nevermind here are my adresses in case you're Jesus.
* Bitcoin: 1GUZ5w7A9PEu8TNrvKfAAaqhABUPW4RjfS
* Ethereum: 0x56D6C69EC22Ee78A0454A165738A20a2e961385d
* Bitcoin Cash: qz5mle4x2vjelax2c0wxhuprq5ha63w4xsj0r38g8s