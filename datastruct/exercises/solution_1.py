from datastruct.classes.lists import LinkedList
from datastruct.classes.lists import Node

def add_two_numbers(l1: LinkedList[int], l2: LinkedList[int]) -> LinkedList[int]:
    result = LinkedList[int]()
    carry = 0

    first = l1.head
    second =  l2.head
    last = None

    while first or second or carry:
        first_val = first.data if first else 0
        second_val = second.data if second else 0

        total = first_val + second_val + carry
        carry = total // 10
        new_node = Node(total % 10)

        if not result.head:
            result.head = new_node
        else:
            last.next = new_node

        last = new_node

        if first:
            first = first.next
        if second:
            second = second.next

    return result
