# THIS IS AN UNFINISHED DEQUE IMPLEMENTATION
from queue import Empty


class ArrayDeque:
    """Deque implementaation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10

    def __init__(self) -> None:
        """Create an empty deque."""
        self._data = [None]*ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in dequq."""
        return self._size
    
    def is_empty(self):
        """Return True if dequq is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the deque is empty."""
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._data(self._front)

    def last(self):
        """Return (but do not remove) the element at the front of the queue.
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Deque is empty.')
        return (self._data(len(self)))

    def add_first(self, first):
        """Add value to beginning of deque."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).
        Raise Empty exception if the queue is empty."""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        """Resize to a new list of capacity >= len(self)."""
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0
    
    # FOR DEQUE USE PYTHON COLLECTIONS LIBRARY (OR IMPLEMENT IT YOURSELF IN A COPY OF THIS FILE)