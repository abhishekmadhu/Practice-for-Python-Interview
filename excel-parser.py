import pandas as pd
import json
import numpy as np
import mpu


def default(o):
    if isinstance(o, np.int64): return str(o)
    raise TypeError


data = pd.read_excel('files/datafile.xlsx')
# print(data.keys())
# for key in data.keys():
#     print(key, end=' ')
# print()
# print(data.values)
#
# for val in data.values:
#         for v in val:
#             print(type(v))
# print(data.iloc[:,:])
# dict = data.to_dict()
# print(dict)
# print(json.dumps(dict, indent=4, sort_keys=True))
keys = [key for key in data.keys()]
values = data.values
print(data.values)
keys_other_than_name = [key for key in data.keys()]
keys_other_than_name.remove('Name')


# print(keys)
# print(keys_other_than_name)

d = {}

for i in range(len(data['Name'])):
    # print(data['Name'][i])
    name = data['Name'][i]
    inner_dict = {}
    for key in keys_other_than_name:
        inner_dict[key] = data[key][i]

    d[name] = inner_dict


print(d)
# print(type(d))
#
j = json.dumps(d, indent=4, default=default)
print(j)

with open('files/output.json', 'w') as outfile:
    json.dump(j, outfile, ensure_ascii=False)

mpu.io.write('files/mpu_output.json', j)