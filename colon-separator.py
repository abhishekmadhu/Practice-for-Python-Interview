x = 'alkdjf:ahdfjlak:adfadsf:adsfa   : kljdslfkja: fasdf fsafadf : adskfjh'

# print(x)
print(x.split(':'))
print(x.strip().split(':'))
print(list(map(lambda x: x.strip(' '), x.strip().split(':'))))
