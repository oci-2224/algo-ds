from typing import TypeVar, Generic
from stack import StackADT

T = TypeVar("T")


class TupleStack(StackADT, Generic[T]):

    """
    Implements a stack ADT by storing the elements in a tuple

    >>> s: TupleStack[int] = TupleStack()
    >>> s.push(3)
    >>> s.push(5)
    >>> s
    (3, 5)
    >>> len(s)
    2
    >>> s.peek()
    5
    >>> s.pop()
    5
    >>> s
    (3,)
    >>> s.pop()
    3
    >>> s
    ()
    >>> s.pop()
    Traceback (most recent call last):
    ...
    IndexError: tuple index out of range

    """

    def __init__(self) -> None:
        self._items: tuple = tuple()

    def push(self, item: T) -> None:
        self._items += (item,)

    def pop(self) -> T:
        value = self._items[-1]
        self._items = self._items[:-1]
        return value

    def peek(self) -> T:
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return repr(self._items)

if __name__ == '__main__':
    try:
        import doctest
        doctest.testmod()
    except:
        print("Use a standard Python interpreter to benefit from doctests")
        
