"""
Создайте программу, которая хранит каталог товаров в виде словаря. Ключами являются названия товаров,
а значениями — другая информация о товаре, например, цена и количество на складе.
Реализуйте функции для добавления, удаления и изменения информации о товаре.
"""

catalog = {
    "Laptop": {"price": 1000, "stock": 5},
    "Phone": {"price": 500, "stock": 10}
}

def add_to_catalog(name, price, stock):
    if name not in catalog:
        catalog[name] = {'price' : price, 'stock' : stock}
        print(f'{name} теперь в каталоге')
    else:
        print(f'{name} уже в каталоге')
# добавить штуку для ред цены и количества

def del_from_catalog(name):
    if name in catalog:
        del catalog[name]
        print(f'Товар "{name}" уделен из каталога')
    else:
         print(f'Товара "{name}" нет в каталоге')


"""
def edit_catalog_by_name(name, price, stock):
    if name in catalog:
        print(f'1. Изменить цену')
        print(f'2. Изменить количество товаров на складе')
        answer = int(input())
        if answer == 1:
            price = int(input(('Введите новую стоимость')))           
            catalog[name]['price'] = price
        if answer == 2:
            stock = int(input(('Введите новое количество товара на складе')))
            catalog[name]['stock'] = stock
        else:
            pass
    else:
        print(f"Товара '{name}' нет в каталоге")
"""

def edit_price_by_name(name, price):
    if name in catalog:          
            catalog[name]['price'] = price
    else:
        print(f"Товара '{name}' нет в каталоге")

def edit_stock_by_name(name, stock):
    if name in catalog:
            catalog[name]['stock'] = stock
    else:
        print(f"Товара '{name}' нет в каталоге")




def show_catalog():
    for name, info in catalog.items():
        print(f'{name} : price: {info["price"]}, stock: {info["stock"]}')
    # print(catalog.items())

def menu():
    while True:
        print('\n', "Выбор действия:")
        print("1. Показать каталог")
        print("2. Удалить товар из каталога")
        print("3. Редактировать стоимость или количество товара")
        print("4. Выйти", '\n')
        n = int(input("Ваш выбор: "))
        print()
        if n == 1:
            show_catalog()
        elif n == 2:
            product = input('Какой товар хотите удалить?')
            del_from_catalog(product)
        elif n == 3:
            product = input('Информацию о каком товаре Вы хотите редактировать?')
            print('1. Изменить стоимость')
            print('2. Изменить количество товара на складе')
            n = int(input('Ваш выбор: '))
            if n == 1:
                new_price = int(input('Какая новая стоимость?'))
                edit_price_by_name(product, new_price)
            elif n == 2:
                new_stock = int(input('Какое количество товара находится на складе?'))
                edit_stock_by_name(product, new_stock)
        elif n == 4:
            break

menu()
