def pet(name,type='dog'):
    """This is the function call by argument"""
    print("I love",type,"Its name is",name)
pet('dog','tom')
pet('tom','dog')
pet(type='dog',name='tom')
pet(name='tom',type='dog')
pet(name='tom')
pet('tom')