promt="\nEnter the name of city you visited: "
while True:
    city=input(promt)
    if city.upper()!='QUITE':
        print("I also love",city)      
        continue
    else:
        print("Bye Bye......")
        break  
