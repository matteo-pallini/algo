from collections import Counter
import string

class Solution:
    def run(self, s: str) -> int:
        alphabet = string.ascii_lowercase
        l_to_v = {l: 2+idx//3 for idx, l in enumerate(alphabet[2:])}
        l_to_v['a'] = 1
        l_to_v['b'] = 1
        whole_string_val = sum(l_to_v[l] for l in s)
        whole_string_len = len(s)
        extra_substrings = {(0,whole_string_len): whole_string_val % whole_string_len == 0}

        queue = [(0, whole_string_len-1, whole_string_val)]

        while queue:
            (start_idx, end_idx, previous_value) = queue.pop(0)
            if end_idx-start_idx > 1:

                left = (start_idx, end_idx-1, previous_value-l_to_v[s[end_idx]])
                left_string = s[left[0]:left[1]+1]
                if (left[0], left[1]) not in extra_substrings:
                    extra_substrings[(left[0], left[1])] = left[2] % len(left_string) == 0
                queue.append(left)

                right = (start_idx + 1, end_idx, previous_value - l_to_v[s[start_idx]])
                right_string = s[right[0]:right[1]+1]
                if (right[0], right[1]) not in extra_substrings:
                    extra_substrings[(right[0], right[1])] = right[2] % len(right_string) == 0
                queue.append(right)

        for idx, letter in enumerate(s):
            extra_substrings[(idx)] = True
        return sum(extra_substrings.values())
