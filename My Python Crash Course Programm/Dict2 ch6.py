lang={'vkj1': 'python', 'Arnav': 'c', 'kj': 'cpp', 'jiya': 'vb', 'chinku': 'rust'}
key1=lang.get('vkj','Yoy dont have such value')
print(key1)
for key,value in lang.items():
    print(f"For key-{key}, value is {value}")