prompt="If yo share your detail, it will help us"
prompt1=prompt+"\nEnter Your Name: "
msg=input(prompt1)
print("Hello",msg.title())
#Code extended
prompt1=prompt+"\nEnter Your Age"
age=input(prompt1)
if age>=18:
    print("Your age is",age,"years, So you can rent a car")
else:
    print("SORRY,You are under age, so you can't rent a car")
        