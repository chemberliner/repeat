from datetime import datetime
from dateutil.relativedelta import relativedelta
import random
import os

def gen_token(login: str, count_month: int) -> str:
    curr_date : datetime = datetime.now()
    end_date = curr_date + relativedelta(months=count_month)
    end_date_string = end_date.strftime('%Y-%m-%d')
    random_int = random.randint(1000000, 9999999)
    token = f"{login}|{end_date_string}|{random_int}"

    return token


def save_token(token: str):
    folder_path = 'D:\\programming\\repeat\\repeat_2'
    file_name = 'token.txt'
    file_path = os.path.join(folder_path, file_name)
    

    with open(file_path, 'a', encoding= 'utf-8') as file:
        file.write(token + '\n')



def get_all_tokens() -> list[str]:
    with open('token.txt', 'r', encoding ='utf-8') as file:
        data = file.readlines()
    # return [t.strip() for t in data]
    return [t[:-1] if t.endswith('\n') else t for t in data] # -1 потому что убираем сам символ(?) переноса строки?



def chek_token(token : str) -> bool:
    all_tokens = get_all_tokens()
    for t in all_tokens:
        if t == token:
            return True
    return False




if __name__ == "__main__":
    print(gen_token("admin", 6))
    print(gen_token("vasya", 12))
    t = gen_token('anna', 12)
    save_token(t)
    print(get_all_tokens())
    t = 'anna|2025-11-24|4406280'
    print(t, chek_token(t))
    print('23', chek_token('23'))
