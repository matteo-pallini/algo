from collections import namedtuple
from typing import List, Optional

Entry = namedtuple('Entry', ['hash', 'key', 'value'])


class HashTable:
    INITIAL_LENGTH = 100
    LENGTHENING_TRIGGER = 0.33

    def __init__(self):
        self._hash_table: List[Optional[Entry]] = self.INITIAL_LENGTH * [None]

    def get_element(self, key: str) -> str:
        index = self._compute_key(key, self._hash_table)
        continue_searching = True
        while continue_searching:
            retrieved_element = self._hash_table[index]
            if retrieved_element is None:
                return None
            elif retrieved_element.key == key and retrieved_element.hash == hash(key):
                continue_searching = False
            else:
                index += 1
        return retrieved_element.value

    def add_element(self, key, value: str) -> None:
        self.lengthening_if_needed()
        index = self._compute_key(key, self._hash_table)
        continue_searching = True
        while continue_searching:
            if self._hash_table[index] is None:
                continue_searching = False
                self._hash_table = self._hash_table[:index] + [Entry(hash(key), key, value)] + self._hash_table[
                                                                                               index + 1:]
            else:
                if self._hash_table[index].key == key and self._hash_table[index].hash == hash(key):
                    continue_searching = False
                else:
                    index += 1
                    if index >= len(self._hash_table):
                        self.lengtheing_list_container()
                        index = self._compute_key(key, self._hash_table)

    def lengthening_if_needed(self):
        filling_rate = sum(e is None for e in self._hash_table) / len(self._hash_table)
        needed = filling_rate < self.LENGTHENING_TRIGGER

        if needed:
            self.lengtheing_list_container()

    def lengtheing_list_container(self):
        _doubled_hash_table: List[Optional[Entry]] = [None] * len(self._hash_table) * 2
        for entry in [e for e in self._hash_table if e is not None]:
            index = self._compute_key(entry.key, _doubled_hash_table)
            _doubled_hash_table = (
                    self._hash_table[:index] +
                    [Entry(hash(entry.key), entry.key, entry.value)] +
                    self._hash_table[index + 1:]
            )
        self._hash_table = _doubled_hash_table

    def _compute_key(self, value, hash_table):
        return hash(value) % len(hash_table) - 1
