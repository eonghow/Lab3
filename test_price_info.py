import price_info

print("test_price_info")

def test_total_cost_shopping():
    result = 46.75
    test_result = price_info.total_cost_shopping()
    assert result == test_result

def test_cost_of_fruit():
    result = 12.0
    test_result = price_info.cost_of_fruits('apple', 10)
    assert result == test_result

