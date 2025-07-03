def string_to_int(string_):
    negative = False
    if string_[0] == "-":
        negative = True

    new_val = 0
    for i, v in enumerate(reversed(string_[negative:])):
        new_val += (ord(v) - ord("0")) * 10 ** i
    return -1 * new_val if negative else new_val


def int_to_string(int_):
    negative = False
    if int_ < 0:
        negative = True
        int_ *= -1

    final_values = []

    while int_ > 0:
        character = chr(ord("0") + int_ % 10)
        final_values.append(character)
        int_ //= 10

    if negative:
        final_values.append("-")

    return "".join(reversed(final_values))
