def rabin_karp(main_text, target_string, base, prime_number):
    target_string_l = len(target_string)
    main_text_l = len(main_text)
    h = base ** (
                target_string_l - 1)  # this is specifying the position for the high order digit of the target_string with length m
    h_mod = h % prime_number  # add module to make number smaller and make more likely that operations happens in constant time
    p = 0  # placeholder for hashed target string
    t = 0  # placeholder for slice of main_text

    for i in range(target_string_l):
        p = (base * p + ord(target_string[i])) % prime_number
        t = (base * t + ord(main_text[i])) % prime_number
    words = [main_text[i] for i in range(target_string_l)]

    for s in range(main_text_l - target_string_l):
        if p == t:
            # given that we using hashes collision is still possible, if a large enough value for prime_number has been
            # used it should be rare
            if target_string == main_text[s:s + target_string_l]:
                return s
        if s < (main_text_l - target_string_l - 1):
            # update main_text hash through rolling hash
            words = words[1:] + [main_text[s + target_string_l]]
            t = (base * (t - ord(main_text[s]) * h_mod) + ord(main_text[s + target_string_l])) % prime_number
