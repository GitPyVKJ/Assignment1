def pizza_top(*toppings):
    """Pass as many parameter as required"""
    print("Making Pizza From Followung Toppings")
    for topping in toppings:
        print(f"- {topping}")
pizza_top('Corn')
pizza_top('Olive','Mashroom','cheese')

