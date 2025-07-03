def spreadsheet_column_checking(col):
    idx = 0
    for i, val in enumerate(reversed(col.lower())):
        idx += (ord(val) - ord("a") + 1) * 26 ** i
    return idx
