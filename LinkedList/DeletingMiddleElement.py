from BasicOperation import LinkedList


def find_middle(head):
    if(head):
        slow = head
        fast = head
        prev = None
        while(slow.next != None and fast.next != None and fast.next.next != None):
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        slow.next = None


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    linked_list = LinkedList()
    for num in list:
        linked_list.insert(num)
    find_middle(linked_list.get_head())
    linked_list.traverse(linked_list.get_head())
