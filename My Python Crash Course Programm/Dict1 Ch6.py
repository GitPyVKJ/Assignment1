lang={'vkj':'python','Arnav':'c','kj':'cpp','jiya':'vb'}
print(f" Mr. Virander, your language is {lang['vkj']}")
lang['chinku']='rust'
print(lang)
del lang['vkj']
print(lang)
print(f"You have just added Chinku who like {lang['chinku'].title()} language.")