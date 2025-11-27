ang={'vkj1': 'python', 'Arnav': 'c', 'kj': 'cpp', 'jiya': 'vb', 'chinku': 'rust'}
lang=['Arnav','chinku']
for name in ang.keys():
    print(f"Hi {name.title()}")
    if name in lang:
        print(f"{name} I see, you like {ang[name].title()} language")
    
