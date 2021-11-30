my_dict = {'key1':'value1', 'key2':'value2'}
print(my_dict)
# {'key1': 'value1', 'key2': 'value2'}
print(my_dict['key1'])
# value1

price_lookups = {'apple':2.99, 'orange':3.56, 'milk':5.80}
print(price_lookups['orange'])
# 3.56

d = {'k1':123, 'k2':[0, 1, 2], 'k3':{'insideKey':100}}
print(d['k2'])
# [0, 1, 2]
print(d['k2'][2])
# 2
print(d.keys())
# dict_keys(['k1', 'k2', 'k3'])
print(d.values())
# dict_values([123, [0, 1, 2], {'insideKey': 100}])

# Grab hello
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])
# hello
