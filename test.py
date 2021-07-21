def test(lst):
    return [x for x in lst if lst.count(x) == 1]


print(test(['a', 'a', 'b', 'c', 'd', 'd']))