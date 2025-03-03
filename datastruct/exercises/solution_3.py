from datastruct.classes.lists import LinkedList


def sort_list_by_insertion(linked_list: LinkedList[int]) -> LinkedList[int]:
    # Implement solution here
    head =  linked_list.head

    temp = head.next

    while head.next is not None:
        if temp < head:
            head = temp

    pass
