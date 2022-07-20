class ListNode:
    def __init__(self,val = 0, next = None):
        self.val = val
        self.next = next


s1 = ListNode(2)
s2 = ListNode(3)
s3 = ListNode(4)
s4 = ListNode(5)

head = s1
s1.next = s2
s2.next = s3
s3.next = s4

tail = None
while head:
    a = ListNode(head.val)
    a.next = tail
    tail = a
    head = head.next

while tail:
    print(tail.val)
    tail = tail.next

