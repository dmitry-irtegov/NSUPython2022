class Storage:
    def __init__(self, initial_value=None):
        self._storage = dict(
            initial_value) if initial_value is not None else dict()

    def edit(self):
        return StorageTransactionManager(self._storage)

    def keys(self):
        return self._storage.keys()

    def __len__(self):
        return len(self._storage)

    def __getitem__(self, key):
        return self._storage[key]

    def __setitem__(self, key, value):
        raise ValueError("Can't set to storage outside transaction block")

    def __str__(self):
        return str(self._storage)

    def __repr__(self):
        return repr(self._storage)


class StorageTransactionManager:
    def __init__(self, storage):
        self._storage = storage

    def __enter__(self):
        self._transaction_data = dict()
        return self

    def __exit__(self, type, value, traceback):
        if type is None:
            self._storage.update(self._transaction_data)
        else:
            return  # forwards exception

    def __getitem__(self, key):
        return self._transaction_data[key] if key in self._transaction_data else self._storage[key]

    def __setitem__(self, key, value):
        self._transaction_data[key] = value
