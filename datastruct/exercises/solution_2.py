from datastruct.classes.lists import LinkedList


def swap_nodes_in_pairs(linked_list: LinkedList[int]) -> LinkedList[int]:
    head = linked_list.head
    ntswap = head.next.next
    head = ntswap

    pass
