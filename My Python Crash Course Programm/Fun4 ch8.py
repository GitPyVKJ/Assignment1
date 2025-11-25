def inputname(f_name,l_name):
    """Take input and print formatted mname in infinite loop"""
    while True:
        print("\nEnter Your Name")
        print("Enter 'q' any time, to quite anytime")
        f_name=input("Enter First Name ")
        if f_name.upper()=='Q':
            break
        print("Enter 'q' any time, to quite anytime")
        l_name=input("Enter Last Name ")
        if l_name.upper()=='Q':
            break
        print (f"{f_name} {l_name}")
inputname('Raj','Tilak')        


