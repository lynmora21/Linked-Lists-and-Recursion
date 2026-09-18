class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        """
        Assign the provided data and initialize next to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        """
        Initialize head to None to represent an empty list.
        """
        self.head = None

    def insert_at_front(self, data):
        """
        Create a new Node and insert it at the front of the list.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Create a new Node and insert it at the end of the list.
        """
        new_node = Node(data)

        # If the list is empty, the new node becomes the head.
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node.
        current = self.head
        while current.next is not None:
            current = current.next

        # Connect the last node to the new node.
        current.next = new_node

    def recursive_sum(self):
        """
        Use recursion to sum all node data in the list.
        """

        def sum_nodes(node):
            # Base case: no node means there is nothing to add.
            if node is None:
                return 0

            # Recursive case: add current data to the rest of the list.
            return node.data + sum_nodes(node.next)

        return sum_nodes(self.head)

    def recursive_reverse(self):
        """
        Reverse the list in-place using recursion.
        """

        def reverse_nodes(prev, current):
            # Base case: reached the end of the list.
            if current is None:
                return prev

            # Save the next node before changing the pointer.
            next_node = current.next

            # Reverse the current node's pointer.
            current.next = prev

            # Recursively reverse the remaining nodes.
            return reverse_nodes(current, next_node)

        # The returned node becomes the new head.
        self.head = reverse_nodes(None, self.head)

    def recursive_search(self, target):
        """
        Return True if target is found, otherwise False, using recursion.
        """

        def search_nodes(node):
            # Base case: reached the end without finding target.
            if node is None:
                return False

            # Target found.
            if node.data == target:
                return True

            # Recursive case: search the next node.
            return search_nodes(node.next)

        return search_nodes(self.head)

    def display(self):
        """
        Print the contents of the list.
        """
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")
