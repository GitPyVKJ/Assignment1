def print_models(unprinted_models,printed_models):
    while unprinted_models:
        current_model=unprinted_models.pop()
        print(f"Current Printed Model: {current_model}")
        printed_models.append(current_model)

def show_printed_models(printed_models):
    print("Printed Models Are:\n")
    for current_model in printed_models:
        print(current_model)
unprinted_models=['Mob Case','Key chain','locket']
printed_models=[]
print_models(unprinted_models,printed_models)
show_printed_models(printed_models)