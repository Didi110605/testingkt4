1. import pytest

@pytest.mark.parametrize("input_number, expected", [
    (999999, False),     
    (-1000000, True),   
    (1, False),          
    (0, True),           
    (2**31 + 1, False)   
])
def test_is_even(input_number, expected):
    assert is_even(input_number) == expected


2. import pytest

@pytest.mark.parametrize("length, width, expected", [
    (1, 0, 0),           
    (0, 0, 0),           
    (1, -1, -1),          
    (3.14159, 2.71, 8.5397299), 
    (10000, 10000, 100000000) 
])
def test_calculate_area(length, width, expected):
    assert calculate_area(length, width) == pytest.approx(expected)


3.import pytest

@pytest.mark.parametrize("a, b, c, expected", [
    (3, 4, 5, "разносторонний"),  
    (1, 1, 1.414, "не треугольник"), 
    (6, 6, 10, "равнобедренный"), 
    (0, 5, 5, "не треугольник"), 
    (-3, 4, 5, "не треугольник"), 
    (3, 3, 3, "равносторонний"),   
    (10, 1, 1, "не треугольник")  
])
def test_classify_triangle(a, b, c, expected):
    assert classify_triangle(a, b, c) == expected
