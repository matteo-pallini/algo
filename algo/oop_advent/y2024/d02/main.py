

def compare(vals: list[int]) -> bool:
    diffs = [v - vals[idx+1] for idx, v in enumerate(vals[:-1])]
    inc = [d > 0 for d in diffs]
    dec = [d < 0 for d in diffs]
    in_range = [1 <= abs(d) <= 3 for d in diffs]
    if all(in_range) and (all(inc) or all(dec)):
        return True
    else:
        return False


if __name__ == "__main__":
    with open("input_full.txt", "rt") as handle:
        safe_list, allow_one_level_failure = [], True
        to_assess = [[int(e) for e in l.split(" ")] for l in handle.readlines()]
        while to_assess:
            vals = to_assess.pop()
            if compare(vals):
                safe_list.append(vals)
            elif allow_one_level_failure:
                passed = False
                for idx in range(len(vals)):
                    if compare(vals[:idx] + vals[idx+1:]):
                        passed = True
                if passed:
                    safe_list.append(vals)
            else:
                pass
        print(len(safe_list))


