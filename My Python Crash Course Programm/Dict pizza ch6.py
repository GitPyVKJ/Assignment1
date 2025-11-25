pizza={'crust':'thick', 
     'toppings':['cheese','mashroom','pepper','olive'] ,
     'sides': ['garlic bread','coke','dip'],
      }
toppings_stock=['cheese','olive','capsicum']
sides_stock=['coke','dip','wings']

print("\n------Your Orderng-------\n")
print(f"Crust-{pizza['crust']}")
print(f"\nToppings-->")
for topp in pizza['toppings']:
    if topp in toppings_stock:
        print(topp)
    else:
        print(f"Sorry, {topp} is not available")    
print(f"\nSides-->")
for sidd in pizza['sides']: 
    if sidd in sides_stock:
        print(sidd)
    else:
        print(f"Sorry, {sidd} is not available")   

print("\n------Your Final Accepted Order-------\n")
print(f"Crust-{pizza['crust']}")
print(f"\nToppings-->")
for topp in pizza['toppings']:
    if topp in toppings_stock:
        print(topp)
print(f"\nSides-->")
for sidd in pizza['sides']: 
    if sidd in sides_stock:
        print(sidd)
