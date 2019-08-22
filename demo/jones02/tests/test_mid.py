from jones02.mid import mid

def test_3_3_5():
    # Given three numbers
    x = 3
    y = 3
    z = 5

    # When: get the middle number
    m = mid(x, y, z)

    # Then:
    assert m == 3

def test_1_2_3():
    # Given three numbers
    x = 1
    y = 2
    z = 3

    # When: get the middle number
    m = mid(x, y, z)

    # Then:
    assert m == 2

def test_3_2_1():
    # Given three numbers
    x = 3
    y = 2
    z = 1

    # When: get the middle number
    m = mid(x, y, z)

    # Then:
    assert m == 2

def test_5_5_5():
    # Given three numbers
    x = 5
    y = 5
    z = 5

    # When: get the middle number
    m = mid(x, y, z)

    # Then:
    assert m == 5

def test_5_3_4():
    # Given three numbers
    x = 5
    y = 3
    z = 4

    # When: get the middle number
    m = mid(x, y, z)

    # Then:
    assert m == 4

def test_2_1_3():
    # Given three numbers
    x = 2
    y = 1
    z = 3

    # When: get the middle number
    m = mid(x, y, z)

    # Then:
    assert m == 2