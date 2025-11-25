aliens=[]
i=5
spd1='slow'
for alien in range(15):
    alien={'color':'green','point':i,'speed':spd1}
    aliens.append(alien) 
    i=i+5
    if i%10==0:
        spd1='fast'
    else:
        spd1='slow'  
i=1
for alien in aliens[:10]:
    print(i, alien)
    i=i+1      
i=1
for alien in aliens[10:]:
    print(i, alien)
    i=i+1      
print("...")
print(len(aliens))



