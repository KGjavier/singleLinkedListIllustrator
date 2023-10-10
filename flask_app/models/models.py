
# Define a Node class representing a node in the linked list
class Node:
    def __init__(self, value, color):
        self.value = value  # Value of the node
        self.color = color  # Color of the node (for styling purposes)
        self.next = None     # Reference to the next node in the linked list

# Define a SingleLinkedList class representing a singly linked list
class SingleLinkedList:
    

    def __init__(self):
        self.head = None   # Reference to the first node in the linked list
        self.length = 0    # Length of the linked list

    # Method to add a new node at the end of the linked list
    def push(self, value, color):
        new_node = Node(value, color)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    # Method to remove the last node from the linked list
    def pop(self):
        if not self.head:
            return None
        elif not self.head.next:
            value = self.head.value
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            value = current.next.value
            current.next = None
        self.length -= 1
        return value

    # Method to remove the first node from the linked list
    def shift(self):
        if not self.head:
            return None
        value = self.head.value
        self.head = self.head.next
        self.length -= 1
        return value

    # Method to add a new node at the beginning of the linked list
    def unshift(self, value, color):
        new_node = Node(value, color)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

    # Method to set the value and color of a node at a specific index
    def set(self, value, color, index):
        if index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value
        current.color = color

    # Method to insert a new node at a specific index -working!!!
    def insert(self, value, color, index):
        if index < 0 or index > self.length:
            return None
        new_node = Node(value, color)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1

    # Method to remove a node at a specific index -working
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            value = self.head.value
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            value = current.next.value
            current.next = current.next.next
        self.length -= 1
        return value

    # Method to reverse the linked list -not working
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    
        # Method to make SingleLinkedList iterable
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

# Example usage:
# Create a SingleLinkedList
my_list = SingleLinkedList()
my_list.push(1, '')
my_list.push(2, '')
my_list.push(3, '')

# Iterate over the nodes in the linked list
for node in my_list:
    print(f"Value: {node.value}, Color: {node.color}")