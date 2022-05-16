def f(arr):
    dic = set()
    for i in arr:
        if i+1 in dic or i-1 in dic:
            return True
        dic.add(i)
    return False


def test():
    assert f([7]) == False
    assert f([4, 3]) == True
    assert f([11, 1, 8, 12, 14]) == True
    assert f([4, 10, 8, 5, 9]) == True
    assert f([5, 5, 5, 5, 5]) == False
