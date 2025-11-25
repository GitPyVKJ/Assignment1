digits=[7,5,1,15,8,21,65,3,77,13,27,9,25]
for value in digits:
    print(f"{digits.pop()}")
print("Orignal List\n")
for value in digits:
    print(value)