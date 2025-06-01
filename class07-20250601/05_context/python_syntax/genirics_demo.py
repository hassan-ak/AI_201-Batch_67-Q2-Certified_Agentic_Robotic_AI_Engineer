# Generics in Python

from typing import TypeVar

T = TypeVar("T")


def first_elemnet(item: list[T]) -> T:
    return item[0]


response01 = first_elemnet([1, 2, 3, 4, 5])
response02 = first_elemnet(["a", "b", "c", "d", "e"])
print("Response 01:", response01)
print("Response 02:", response02)

K = TypeVar("K")
V = TypeVar("V")


def get_value(container: dict[K, V], key: K) -> V:
    return container[key]


response03 = get_value({"a": 2, "b": 3}, "a")
print("Response 03:", response03)


# Generics in Classes
from dataclasses import dataclass, field
from typing import TypeVar, ClassVar, Generic

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)
    
    def pop(self)->T:
        return self.items.pop()
    
    def push(self, item:T)->None:
        self.items.append(item)

stack_of_ints = Stack[int]()
print(stack_of_ints)
stack_of_ints.push(25)
stack_of_ints.push(7)
print(stack_of_ints)
print(stack_of_ints.pop())
print(stack_of_ints.items)


