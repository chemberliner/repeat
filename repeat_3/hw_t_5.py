"""
Условие:
Создайте программу, которая принимает два списка друзей двух пользователей и возвращает список их общих друзей.
"""
friends_user1 = ["Alice", "Bob", "Charlie"]
friends_user2 = ["Bob", "David", "Charlie"]

def common_friends(lst1 : list, lst2 : list) -> set:
    set1 = set(lst1)
    set2 = set(lst2)
    
    c_f = set1.intersection(set2)
    return c_f

def test_common_friends():
    assert common_friends({"Alice", "Bob", "Charlie"}, {"Bob", "David", "Charlie"}) == {"Bob", "Charlie"}
    assert common_friends({"Alice", "Bob"}, {"David", "Charlie"}) == set()
    assert common_friends(set(), set()) == set()

test_common_friends()
