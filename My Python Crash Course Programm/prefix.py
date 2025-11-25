prefix='http:\\www.google.com\home_page'
print(prefix)
print(prefix.removeprefix('http:\\'))
print(prefix.removesuffix('\home_page'))
prefix=prefix.removeprefix('http:\\')
print(prefix.removesuffix('\home_page'))