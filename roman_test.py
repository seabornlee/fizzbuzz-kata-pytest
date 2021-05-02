import pytest

def roman(number):
    map = {
      5: 'V',
      10: 'X'
    }
    if number in map.keys():
        return map[number]
    if number + 1 in map.keys():
        return roman(1) + roman(number + 1) 
    if number -1 in map.keys():
        return roman(number -1)+roman(1)
    if number -2 in map.keys():
        return roman(number - 2)+roman(2)
    if number -3 in map.keys():
        return roman(number - 3)+roman(3)
    return 'I' * number

@pytest.mark.parametrize('input,expected', [
    (1, "I"),
    (2, "II"),
    (3, "III"),
    (4, "IV"),
    (5, "V"),
    (6, "VI"),
    (7, "VII"),
    (8, "VIII"),
    (9, "IX"),
    (10, "X"),
])
def test_should_covert_number_to_roman(input, expected):
    assert roman(input) == expected 
