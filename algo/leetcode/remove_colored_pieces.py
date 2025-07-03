# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

def winnerOfGame(self, colors: str) -> bool:
    counter = {"A": 0, "B": 0}
    counter = 0
    for idx in range(len(colors)-2):
        pre, current, post = colors[idx:idx+3]
        if pre == current == post:
            if current == "A":
                counter += 1
            else:
                counter -= 1
    return counter > 0
