
from abc import ABC, abstractmethod
from typing import TypeVar, Generic

T = TypeVar('T')

class StackADT(ABC, Generic[T]):

    @abstractmethod
    def push(self, item: T) -> None:
        pass


    @abstractmethod
    def pop(self) -> T:
        pass


    @abstractmethod
    def peek(self) -> T:
        pass


    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __repr__(self) -> str:
        pass


    @abstractmethod
    def is_empty(self) -> bool:
        pass


class ListStack(StackADT, Generic[T]):
    '''

    ``ListStack`` implements a stack by using a list as the container.

    >>> s: ListStack[int] = ListStack()
    >>> s.push(1)
    >>> s
    [1]
    >>> s.push(2)
    >>> s
    [1, 2]
    >>> s.push(3)
    >>> s
    [1, 2, 3]
    >>> s.peek()
    3
    >>> s.pop()
    3
    >>> s
    [1, 2]
    >>> s.pop()
    2
    >>> s.pop()
    1
    >>> s
    []

    '''

    def __init__(self) -> None:
        self._items: list[T] = []

    def __repr__(self) -> str:
        return repr(self._items)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
