def test_is_subset():
    assert is_subset({1, 2, 3}, {1, 2, 3, 4, 5}) == True
    assert is_subset({1, 2, 3}, {4, 5, 6}) == False
    assert is_subset(set(), {1, 2, 3}) == True
    assert is_subset({10, 11, 12}, {12, 13,14}) == False
    assert is_subset({5, 8, 12}, {6, 9, 10}) == False
    assert is_subset({1, 2}, {1, 2}) == True
    assert is_subset({1, 2, 3, 4, 5}, {3, 4, 5}) == True
    print('OK')

# рабочий
"""
def is_subset(s1 : set, s2 : set) -> bool:
    if s1.intersection(s2) == s1 or s1.intersection(s2) == s2:
        return True
    else:
        return False
"""
# рабочий
"""
def is_subset(s1: set, s2: set) -> bool:
    flag = all(el in s2 for el in s1)
    if not flag:
        flag = all(el in s1 for el in s2)

    return flag
"""

def is_subset(s1 : set, s2 : set) -> bool:
    for el in s1:
        if el not in s2:
            for el in s2:
                if el not in s1:
                    return False

    return True


test_is_subset()