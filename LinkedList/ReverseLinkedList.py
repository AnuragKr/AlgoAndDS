class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        node = Node(data)

        if(self.head is None):
            self.head = node
            return self.head

        q = self.head
        while(q.next != None):
            q = q.next
        q.next = node
        return self.head

    def traverse(self):
        if(self.head):
            while(self.head != None):
                print(self.head.data)
                self.head = self.head.next


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    linked_list = LinkedList()
    for num in list:
        linked_list.insert(num)
    linked_list.traverse()
