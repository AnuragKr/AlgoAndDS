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

    def traverse(self, head):
        if(head):
            while(head != None):
                print(head.data)
                head = head.next

    def get_head(self):
        return self.head
