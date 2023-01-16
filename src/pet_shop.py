def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, total_amount):
    pet_shop["admin"]["total_cash"] += total_amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, num):
    pet_shop["admin"]["pets_sold"]+= num


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, pet_breed):
    pet_breed_search = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            pet_breed_search.append(pet)
    return pet_breed_search
            

def find_pet_by_name(pet_shop, pet_name):
    for pets in pet_shop["pets"]:
        if pets["name"] == pet_name:
            return pets

def remove_pet_by_name(pet_shop, pet):
    return pet_shop["pets"].pop(3)

def add_pet_to_stock(pet_shop, new_pet):
    return pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer, sub_amount):
    customer["cash"] -= sub_amount

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    return customers["pets"].append(new_pet)