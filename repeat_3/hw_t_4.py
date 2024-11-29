def unique_elements(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)

    union = set1.union(set2)
    intersection = set1.intersection(set2)
    final = union.difference(intersection)
    return list(final)

def test_unique_elements():
    assert unique_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [1, 2, 5, 6]
    assert unique_elements([], [1, 2, 3]) == [1, 2, 3]
    assert unique_elements([1, 2, 3], [1, 2, 3]) == []

# unique_elements(input(), input())
test_unique_elements()