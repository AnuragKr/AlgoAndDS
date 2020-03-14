from BasicOperation import LinkedList


def reverse(head):
    if(head is not None):
        prev = None
        q = head
        while(q is not None):
            p = q
            q = q.next
            p.next = prev
            prev = p
        return prev
    return None


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    linked_list = LinkedList()
    for num in list:
        linked_list.insert(num)
    reverse_head = reverse(linked_list.head)
    linked_list.traverse(reverse_head)
