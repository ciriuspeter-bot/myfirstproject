list = []
def identify(str):
    list = str.lower().split()
    new_str = ''.join(list)
    return new_str[::-1]
print(identify("asdfojfwllll"))
    