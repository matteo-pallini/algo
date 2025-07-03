def check_palindrome(string):
    if len(string) <= 1:
        return False
    letters_counter = [0] * 256
    for letter in string:
        letters_counter[ord(letter)] = (letters_counter[ord(letter)] + 1) % 2
    if sum(letters_counter) > 1:
        return False
    else:
        return True


def check_palindrome_better(string):
    odd_count = 0
    if len(string) <= 1:
        return False
    letters_counter = [0] * 256
    for letter in string:
        letters_counter[ord(letter)] += 1
        if letters_counter[ord(letter)] % 2 == 0:
            odd_count -= 1
        else:
            odd_count += 1
    print(odd_count)
    return odd_count <= 1
