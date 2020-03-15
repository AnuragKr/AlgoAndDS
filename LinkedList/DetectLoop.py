from BasicOperation import LinkedList


def find_loop(head):
    if(head):
        slow = head
        fast = head
        while(slow.next and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                print("Loop Detected")
                break
    print("Loop Not Found")


if __name__ == "__main__":
    list = [1, 2, 3, 4, 5]
    linked_list = LinkedList()
    for num in list:
        linked_list.insert(num)
    find_loop(linked_list.get_head())
