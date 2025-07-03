def intercovert(value):
    int_to_string = {i: str(i) for i in range(10)}
    string_to_int = {str(i): i for i in range(10)}

    if isinstance(value, int):
        new_value = []
        negative = value < 0
        value = value * -1 if negative else value
        while value > 0:
            decimal = value % 10
            value = (value - decimal)//10
            new_value.append(int_to_string[decimal])
        final_val = "".join(new_value[::-1])
        return "-"+final_val if negative else final_val
    else:
        new_value = 0
        negative = value[0] == "-"
        if value[0] == "-":
            negative = True
            value = value[1:]
        else:
            negative = False
        value_len = len(value)-1
        for idx, e in enumerate(value):
            new_value += string_to_int[e] * 10**(value_len-idx)
        return -1*new_value if negative else new_value
