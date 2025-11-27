#sort=permanent, sorted=temp sort,reverse,length
cars=['maruti','ducati','kia','toyota','ferari','honda','ford']
print("Following is the orignal list \n",cars)
sorted_cars=sorted(cars)
print("Following is the temp sorted list \n",sorted_cars)
print("Following is the again orignal list \n",cars)
cars.sort()
print("Following is the permanent sorted list \n",cars)
cars.sort(reverse=True)
print("Following is the reverse sorted list \n",cars)
length=len(cars)
print(length)
