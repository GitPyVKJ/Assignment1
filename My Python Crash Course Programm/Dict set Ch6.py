ang={'vkj':'python', 
     'Arnav':'c', 
     'kj':'cpp', 
     'jiya':'python', 
     'chinku':'rust'
     }

print("\nSorted Names are:")
for name in sorted(ang.values()):
    print(name.title())
print("\nSet Names are:")
for name in set(ang.values()):
    print(name.title())
print("\nSorted Set Names are:")
for name in sorted(set(ang.values())):
    print(name.title())