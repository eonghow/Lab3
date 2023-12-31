import Lab3

print("Test_Lab3")

def test_bubble_sort_ascending():
    result = []
    arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

<<<<<<< HEAD
def test_large_number():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90, 5, 6, 7]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == 1)

def test_no_number():
    result = []
=======
def test_empty_array():
>>>>>>> 91ffec86cf83efc7e2cd50cb36e49724c9b24987
    input_arr = []
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 0)

<<<<<<< HEAD
def test_alphabets():
    result = []
    input_arr = [64, 333, 6, "abh", 33, 22, 3, 8]
=======
def test_large_array():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 43, 56, 78, 9, 8, 7, 6, 5]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 1)

def test_large_array():
    input_arr = [64, "abc", 25, 12, 22, 11, 90]
>>>>>>> 91ffec86cf83efc7e2cd50cb36e49724c9b24987
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 2)