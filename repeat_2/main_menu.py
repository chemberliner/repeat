from utils import chek_token, gen_token, save_token


#from datetime import datetime
#from dateutil.relativedelta import relativedelta

def read_user_token():
    token = input("Введите код абонемента:")
    token_is_valid = False


    if chek_token(token):
        token_is_valid = True

    if token_is_valid:
        print("Добро пожаловать!")
        el = token.split('|')
        print(f"{el[0]}, Ваш абонемент действует до {el[1]}, его уникальный номер: {el[2]}")

    else:
        print("Абонемент не действителен. Купите новый!")
    

def bye_token():
    print()
    login = input("Ваш логин: ")
    print("1. Подписка на 6 месяцев")
    print("2. Подписка на 12 месяцев")
    print("3. Назад")
    n = int(input("Ваш выбор: "))
    if n == 1:
        token = gen_token(login, 6)
        save_token(token)
        print('Ваш абонемент:', token)
    elif n == 2:
        token = gen_token(login, 12)
        save_token(token)
        print('Ваш абонемент:', token)
    elif n == 3:
        return



def menu():
    while True:
        print('\n', "Выбор действия:")
        print("1. Предоставить абонемент")
        print("2. Купить абонемент")
        print("3. Выйти", '\n')
        n = int(input("Ваш выбор: "))
        print()
        if n == 1:
            read_user_token()
        elif n == 2:
            bye_token()
        elif n == 3:
            break
