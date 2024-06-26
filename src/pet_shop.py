def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    total_cash = 0
    total_cash += pet_shop["admin"]["total_cash"] 

    return total_cash

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"] 

def increase_pets_sold(pet_shop, new_pets):
    pet_shop["admin"]["pets_sold"] += new_pets

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, pet_breed):
    pet_breed_search = []
    for pet in pet_shop["pets"]:
        if pet.get("breed") == pet_breed:
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

def get_customer_cash(customer_cash):
    return customer_cash["cash"]

def remove_customer_cash(customer, amount):
    customer ["cash"] -= amount

def get_customer_pet_count(customer_pets):
    return len(customer_pets["pets"])

def add_pet_to_customer(customer, new_pet):
    return customer["pets"].append(new_pet)

def customer_can_afford_pet(customer, new_pet):
    return customer["cash"] >= new_pet["price"]

def sell_pet_to_customer(pet_shop, pet, customer):
    if pet != None and customer_can_afford_pet(customer, pet):
        remove_pet_by_name(pet_shop, pet["name"])
        add_pet_to_customer(customer, pet)
        remove_customer_cash(customer, pet["price"])
        add_or_remove_cash(pet_shop, pet["price"])
        increase_pets_sold(pet_shop, 1)