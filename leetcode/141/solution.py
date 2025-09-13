class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def solution(head: list[ListNode]) -> bool:
    current = head
    while current and current.next:
        if hasattr(current, "seen"):
            return True
        current.seen = "true"
        current = current.next
    return False
