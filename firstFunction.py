def make_name(first_name, middle_name, second_name):
    full_name = first_name + " " + middle_name + " " + second_name
    return full_name.title()
foreign = make_name("Ahmed", "Abas", "Shahd")
print(foreign)   