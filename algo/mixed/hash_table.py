class Dictionary(object):
    """
    implementation for dict
    source: https://csrgxtu.github.io/2020/04/21/Python-Dict-a-new-implementation-by-pure-Python/
    """

    def __init__(self, size=1000):
        """
        use list as storage, each element is also a list which is used
        to solve hash conflict
        """
        self.storage = [[] for _ in range(size)]
        self.size = size
        self.length = 0

    def __setitem__(self, key, value):
        """
        set key value, if it conflicts, append to the sub list
        """
        if self.length + 1 > self.size:
            new_size = self.size * 2
            new_storage = [[] for _ in range(new_size)]
            self.length = self._fill_new_storage(self.storage, new_storage, new_size)
            self.storage, self.size = new_storage, new_size

        self.length = self._set_key(key, value, self.storage, self.size, self.length)

    def _fill_new_storage(self, old_storage, new_storage, size):
        length = 0
        for e in old_storage:
            for (key, value) in e:
                length = self._set_key(key, value, new_storage, size, length)
        return length

    @classmethod
    def _set_key(cls, key, value, storage, size, length):
        storage_idx = hash(key) % size
        for ele in storage[storage_idx]:
            if key == ele[0]:  # already exist, update it
                ele[1] = value
                break
        else:
            storage[storage_idx].append([key, value])
            length += 1
        return length

    def __getitem__(self, key):
        """
        get by key, if not found, raise key error
        :raise: KeyError
        :return: value
        """
        storage_idx = hash(key) % self.size
        for ele in self.storage[storage_idx]:
            if ele[0] == key:
                return ele[1]

        raise KeyError('Key {} dont exist'.format(key))

    def __delitem__(self, key):
        storage_idx = hash(key) % self.size
        for idx, e in enumerate(self.storage[storage_idx]):
            if e[0] == key:
                del self.storage[storage_idx][idx]
                self.length -= 1
                return
        raise KeyError(f"Key {key} doesn't exist")

    def __contains__(self, key):
        try:
            self[key]
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.length
