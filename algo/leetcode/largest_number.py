# https://leetcode.com/problems/largest-number/

class Node:

    def __init__(self, value):
        self.value: str = value
        self.counter = 0
        self.childred = {}

    def get_ordered_numbers(self):
        numbers = [self.value * self.counter]
        sorted_children = sorted(
            self.childred.items(), reverse=True, key=lambda x: x[0]
        )
        children = [
            self.value+child for (k, node) in sorted_children for child in node.get_ordered_numbers()]
        return numbers + children


def largestNumber(self, nums: List[int]) -> str:
    tries = {}
    for e in nums:
        e = str(e)
        tries_pointer = tries
        while e:
            digit, e = int(e[0]), e[1:]
            if digit not in tries_pointer:
                tries_pointer[digit] = Node(value=str(digit))
            node = tries_pointer[digit]
            if len(e) > 0:
                tries_pointer = node.childred
            else:
                node.counter += 1
    final_vals = []
    for (k, v) in sorted(tries.items(), reverse=True, key=lambda x: x[0]):
        final_vals.extend(v.get_ordered_numbers())
    return "".join(final_vals)
