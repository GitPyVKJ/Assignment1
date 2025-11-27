avail=['peproni','cheese','olive','ham','soya','mushroom','green pepper']
req=['peproni','chicken','ham','cheese']
for rq in req:
    if rq in avail:
        print(f"Adding {rq.title()}")
    else:
        print(f"Sorry, We don't have {rq.upper()}")
print("\nWe are Preparing Pizza with Your requested toppings") 

