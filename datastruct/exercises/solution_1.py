from datastruct.classes.lists import LinkedList
from datastruct.classes.lists import Node

def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    l1_data = l1.reverse()
    l2_data = l2.reverse()
    result = []

    result_data = l1.head + l2.head
    return result
    pass

l1 = LinkedList()
l2 = LinkedList()

l1.insert(2)
l1.insert(4)
l1.insert(3)
l2.insert(5)
l2.insert(6)
l2.insert(4)


print(l1)