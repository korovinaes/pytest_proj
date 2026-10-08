from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 0, "test") == 1
    assert arrs.get([1, 2, 3], 2, "test") == 3
    assert arrs.get([1, 2, 3], 3, "test") == "test"
    assert arrs.get([1, 2, 3], 10, "test") == "test"
    assert arrs.get([1, 2, 3], -1, "test") == "test"  # если проверяем текущее поведение
    assert arrs.get([1, 2, 3], 10) is None  # default не передан


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], None, 2) == [1, 2]
    assert arrs.my_slice([1, 2, 3], 0, 10) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], 0, 3) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3], 3) == []
    assert arrs.my_slice([1, 2, 3], 10) == []
    assert arrs.my_slice([1, 2, 3], 2, 1) == []
    assert arrs.my_slice([1, 2, 3], 1, 1) == []
    assert arrs.my_slice([1, 2, 3], 0, 0) == []
    assert arrs.my_slice([1, 2, 3, 4], -2) == [3, 4]
    assert arrs.my_slice([1, 2, 3, 4], 0, -1) == [1, 2, 3]
    assert arrs.my_slice([1, 2, 3, 4], -3, -1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], None, -1) == [1, 2]
