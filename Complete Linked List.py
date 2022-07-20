#ToDo
#To know what is __name__ =="__main"
#__Name__ idnothing but the entry point for the python file, if we are using 2 different python file
# then __name__ value is called funtion name
# 1. Create a node Class
# 2. Create a Linked List Class
# 3. Methods to be defined inside Linked List
# a. Get Length
# b. Insert at end
# c. Insert at start
# d. Insert at one position
# e. Remove at one positon

#1. Create a node Class

class Node:
    def __init__(self, data = None, next =None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_at_start(self,number):
        node = Node(number, self.head)
        self.head = node

    def add_at_end(self,number):
        if self.head == None:
            self.head = Node(number,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(number, None)

    def get_length(self):
        count =0
        if self.head == None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr:
            itr = itr.next
            count+=1
        return count

    def insert_at(self,index,value):
        if index<0 or index> self.get_length()-1:
            return "Not Possible"
        itr = self.head
        count = 0
        if index ==0:
            self.head = Node(value, self.head)
        while itr:
            if count == index-1:
                itr.next = Node(value, itr.next)
                break
            itr = itr.next
            count+=1

    def remove_at(self,index):
        if index<0 or index> self.get_length()-1:
            return "Not Possible"

        itr = self.head


        if index == 0:
            self.head = itr.next
            return
        count = 0
        while itr:
            if count == index-1:
                itr.next = itr.next.next
            count += 1
            itr = itr.next

    def print(self):
        if self.head == None:
            print("Empty Linked List")
            return
        string =''
        itr = self.head
        while itr:
            string += str(itr.data)+"-->"
            itr = itr.next
        print(string)

    def insert_these(self,values):

        for data in values:
            self.add_at_end(data)

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        count =0
        while itr:
            if data_after == itr.data:
                for data in data_to_insert:
                    count += 1

                    self.insert_at(count,data)


                return
            count += 1

            itr = itr.next
        return "No such value inside the list"




    # Search for first occurance of data_after value in linked list
    # Now insert data_to_insert after data_after node

    def remove_by_value(self, data):
        itr = self.head
        count =0
        while itr:
            if itr.data == data:
                self.remove_at(count)
                return
            count += 1
            itr = itr.next
        return "Given data is Not there in the list"





# Remove first node that contains data

if __name__ == "__main__":
    ll = LinkedList()
    ll.add_at_end(2)
    ll.add_at_end(5)
    ll.add_at_end(65)
    ll.print()
    ll.add_at_start(54)
    ll.add_at_start(26)
    ll.print()
    ll.insert_these([1,2,3,4,5,6])
    ll.print()
    print("CURRENT Value",ll.get_length())
    ll.insert_at(4,1000)
    ll.print()
    ll.remove_at(6)
    ll.print()
    ll.remove_at(0)
    ll.print()
    ll.insert_after_value(54,[45,85,995,645,6565,6969])
    ll.print()
    ll.remove_by_value(645)
    ll.print()















