

class Trie:

    def __init__(self):
        self._main_dict = {}
        self._stop_character = "*"

    def insert(self, word):
        temp_dict = self._main_dict
        for letter in word:
            temp_dict = temp_dict.setdefault(letter, {})
        _ = temp_dict.setdefault(self._stop_character, {})

    def insert_many(self, words):
        for word in words:
            self.insert(word)

    def search(self, word):
        temp_dict = self._main_dict
        for letter in word:
            if letter in temp_dict:
                temp_dict = temp_dict[letter]
            else:
                return False
        return self._stop_character in temp_dict