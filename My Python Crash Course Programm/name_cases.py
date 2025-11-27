name="Hello eric"
print(name, "Line2")

print(name.title(), "Line4")

print(name.upper(), "Line6")

print(name.title(),"\n", name.lower(),"\t",name.upper(),  "Line8")

fname="eric"
lname="mathhew"
fullname=fname,lname
print(fullname,  "Line13")
fullname=f"{fname.title()} {lname.title()}"
print(fullname,  "Line15")
print(f"Full Name is {fname.title()} {lname.title()}  Line16")
print("Full Name is", f'"{fname.title()} {lname.title()}"'  " Line17")
