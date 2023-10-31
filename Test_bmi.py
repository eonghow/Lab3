from lab2.bmi import calculate_bmi

def test_bmi_normal_weight():
    result = calculate_bmi(1.70, 55)
    assert (result == 0)

def test_bmi_over_weight():
    result = calculate_bmi(1.75, 100)
    assert (result == 1)

def test_bmi_under_weight():
    result = calculate_bmi(1.50, 40)
    assert (result == -1)
