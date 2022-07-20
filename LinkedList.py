class Node:
    def __init__(self, data = None, next =None):
        self.data =data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self,string):
        self.head =None
        for data in string:
            self.insert_at_end(data)

    def count_no_elements(self):
        count = 0
        itr = self.head
        while(itr.next):
            count+=1
            itr = itr.next
        return count+1

    def remove_at(self, index):
        if index <0 or index>= self.count_no_elements():
            raise "Not Possible, index out of range"
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr = itr.next
                count += 1
        itr.head = itr.head.next


    def insert_at(self):
        pass






    def print(self):
        if self.head is None:
            print("Link List is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll =LinkedList()
    ll.insert_values(["Rama","Sita","Lakshman","Hanuman"])
    ll.print()
    ll.count_no_elements()
    ll.remove_at(2)
    ll.print()
