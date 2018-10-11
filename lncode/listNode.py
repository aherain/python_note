
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def recurse(head, newhead):
    if head is None:
        return
    if head.next is None:
        newhead = head

    else:
        newhead = recurse(head.next, newhead)
        head.next.next = head
        head.next = None

    return newhead

head = ListNode(1)
p1 = ListNode(2)
p2 = ListNode(3)
p3 = ListNode(4)

head.next = p1
p1.next = p2
p2.next = p3

newhead = None
p=recurse(head, newhead)
while p:
    print(p.val)
    p = p.next
