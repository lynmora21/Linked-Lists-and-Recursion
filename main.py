from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    linked_list = LinkedList()

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    linked_list.insert_at_end(101)
    linked_list.insert_at_end(205)
    linked_list.insert_at_end(309)
    linked_list.insert_at_end(412)
    linked_list.insert_at_end(518)

    # TODO: 3) Display the list to verify insertion
    print("Initial Linked List:")
    linked_list.display()

    # TODO: 4) Call recursive_sum and print the result
    total = linked_list.recursive_sum()
    print(f"\nSum of all IDs: {total}")

    # TODO: 5) Call recursive_search with a target and print result
    target = 309
    found = linked_list.recursive_search(target)

    if found:
        print(f"Search for ID {target}: ID found!")
    else:
        print(f"Search for ID {target}: ID not found.")

    # TODO: 6) Call recursive_reverse, then display the reversed list
    linked_list.recursive_reverse()

    print("\nReversed Linked List:")
    linked_list.display()
