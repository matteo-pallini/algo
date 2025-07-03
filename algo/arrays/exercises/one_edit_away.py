def one_edit_away(word_1, word_2):
    word_1_len, word_2_len = len(word_1), len(word_2)
    distance = abs(word_1_len - word_2_len)
    if distance > 1:
        return False
    edits = 0
    offset_1 = 0
    offset_2 = 0
    length = min([word_1_len, word_2_len])
    for idx in range(length):

        letter_1 = word_1[idx + offset_1]
        letter_2 = word_2[idx + offset_2]
        print(letter_1, letter_2)
        if letter_1 != letter_2:
            edits += 1
            if edits > 1:
                return False
            if letter_1 == word_2[idx + offset_2 + 1]:
                offset_2 += 1
            elif word_1[idx + offset_1 + 1] == letter_2:
                offset_1 += 1
            if (idx + offset_1 + 1 > word_1_len) or (idx + offset_2 + 1 > word_2_len):
                if 2 * (idx + offset_1 + offset_2) - word_1_len - word_2_len + (1 - max(edits, 0)) == 0:
                    return True
                else:
                    print("here")
                    return False

    return True
