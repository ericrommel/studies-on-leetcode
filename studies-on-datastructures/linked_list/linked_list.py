class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def append(self, new_node):
        current = self.head
        if current:
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node

    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current:
                if current.value == value:
                    break
                prev = current
                current = current.next
            if current is None:
                return
            prev.next = current.next
            current = None

    def insert(self, new_element, position):
        """
        Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between the 2nd and 3rd elements.
        """
        count = 1
        current = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while current:
            if count + 1 == position:
                new_element.next = current.next
                current.next = new_element
                return
            else:
                count += 1
                current = current.next
        pass

    def show_elements(self):
        current = self.head
        while current:
            print(f"{current.value}--->", end=" ")
            current = current.next
        print(f"{None}")

e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
e5 = Node(5)
e6 = Node(6)
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)
ll.append(e4)
ll.delete(e3.value)
ll.insert(e3, 1)
ll.insert(e5, 3)
ll.show_elements()