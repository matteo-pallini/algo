def phone_mnemonics(numbers):
    mapping = {
        "0": "",
        "1": "",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    if numbers:
        new_combinations = []
        letters = mapping[numbers[0]]
        for l in letters:
            other_combinations = phone_mnemonics(numbers[1:])
            for c in other_combinations:
                new_combinations.append(l+c)
        return new_combinations
    else:
        return [""]