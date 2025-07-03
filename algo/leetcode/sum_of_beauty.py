import math


def sum_of_beauty(nums):
    mins, maxs, min_v,  max_v = [], [], 0, math.inf
    for v in nums:
        if v > min_v:
            min_v = v
        mins.append(min_v)
    for v in nums[::-1]:
        if v < max_v:
            max_v = v
        maxs.append(max_v)
    maxs = maxs[::-1]
    final_score = 0
    for idx, (min_v, v, max_v) in enumerate(zip(mins, nums[1:-1], maxs[2:])):
        if min_v < v < max_v:
            final_score += 2
        elif nums[idx] < v < nums[idx+2]:
            final_score += 1
        else:
            pass
    return final_score
