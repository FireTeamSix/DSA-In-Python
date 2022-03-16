import ctypes


class DynamicArray:
    """Simplified Python List"""

    def __init__(self):
        """Creates empty array"""
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def __len__(self):
        """Returns number of items stored in array"""
        return self._n

    def __getitem__(self, k):
        """Returns item at element k"""
        if not 0 <= k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        """Adds object to end of array"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _make_array(self, c):
        """Return new array with capacity c"""
        return (c * ctypes.py_object)()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightware"""
        # for simplicity we assume 0<=k<=n in this version
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j-1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        """Remove first occurrence of value"""
        # note: we do not consider shrinking the dynamic array in this version
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None
                self._n -= 1
                return
        raise ValueError('value not found')