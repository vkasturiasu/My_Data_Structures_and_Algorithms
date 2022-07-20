class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

a =  ListNode(2)
def splitListToParts(head, k):
    # count no of values in list
    temp, count = head, 0
    while temp:
        temp, count = temp.next, count + 1

    quo, rem = count // k, count % k
    output = [quo + 1] * rem + [quo] * (k - rem)

    prev, temp = None, head

    for index, value in enumerate(output):
        if prev:
            prev.next = None

        output[index] = temp

        for i in range(value):
            prev, temp = temp, temp.next
    return output
