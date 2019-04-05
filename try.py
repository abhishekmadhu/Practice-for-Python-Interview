import pandas as pd
import json

data = pd.read_excel('../files/datafile.xlsx')
print(data)

keys = [k for k in data.keys()]
keys.remove('Name')

for i in range(len(data['Name'])):
    pass

print(keys)



