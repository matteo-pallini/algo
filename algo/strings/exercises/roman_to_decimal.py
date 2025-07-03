
def roman_to_decimal(roman):
    mapping = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    i = 0
    value = 0

    while i < len(roman) -1:
        first_value = mapping[roman[i]]
        second_value = mapping[roman[i+1]]
        if first_value >= second_value:
            value += first_value
            i += 1
        else:
            value += second_value - first_value
            i += 2
    if i < len(roman):
        value += mapping[roman[-1]]
    return value
