def formatted_name(f_name,l_name,m_name=""):
    """Function with return value"""
    if m_name:
        formatted_name=(f"{f_name} {m_name} {l_name}")
    else:
        formatted_name=(f"{f_name} {l_name}")
    return(formatted_name)
name=formatted_name('Virander','Kumar','Joharwal')
print(name)
name=formatted_name('Virander','Joharwal')
print(name)

