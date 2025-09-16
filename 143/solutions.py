# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def solution():
    def reorderList(head: ListNode) -> None:
        pointer = head
        values = []
        while pointer:
            values.append(pointer.val)

        pointer = head
        i = 0
        n = len(values)
        while i <= (n - 1) // 2 and pointer != None:
            Li = values[i]
            Ln_minus_i = values[(n - 1) - i]
            pointer.val = values[Li]
            pointer = pointer.next
            if pointer:
                pointer.val = values[Ln_minus_i]
                pointer = pointer.next
