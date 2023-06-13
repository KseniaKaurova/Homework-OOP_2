def create_cook_book(self):
    with open('recipes.txt', 'rt') as file:
        cook_book = {}
        for s in file:
            meal = s.strip()
            quantity_ingredients = int(file.readline())
            ingredients = []
            for _ in range(quantity_ingredients):
                ingredient_name, quantity, measure = file.readline().split(' | ')
                ingredients.append({
                    'ingredient_name': ingredient_name,
                    'quantity': quantity,
                    'measure': measure
                })
            file.readline()
            cook_book[meal] = ingredients

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for ingredient in cook_book[dishes]:
        ingredient_name = ingredient['ingredient_name']
        quantity = ingredient['quantity'] * person_count
        measure = ingredient['measure']
        if ingredient_name in shop_list:
            shop_list[ingredient_name][quantity] += quantity
        else:
            shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

    return shop_list


def files(self):
    lst = []
    for name in names:
        with open(name, 'r') as file:
            lst.append([name, str(len(file.readlines())), [file.readlines()]])
    sorted(lst, key=lambda x: x[1])
    with open('File.txt', 'w', encoding='utf-8') as file:
        new_file = file.writelines(lst)

    return new_file


names = ['1.txt', '2.txt', '3.txt']
