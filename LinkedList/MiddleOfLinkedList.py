from BasicOperation import LinkedList


def find_middle(head):
    if(head):
        slow = head
        fast = head
        while(slow != None and fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        print(slow.data)


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    linked_list = LinkedList()
    for num in list:
        linked_list.insert(num)
    find_middle(linked_list.get_head())
