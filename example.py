def cars(brand, cartype, **etc):
    profile = {}
    profile["brand"] = brand
    profile["cartype"] = cartype
    for key, value in etc.items():
        profile[key] = value
        return profile
car = cars("Lexus", "Red", color='blue', tow_pacakge=True)
print(car)