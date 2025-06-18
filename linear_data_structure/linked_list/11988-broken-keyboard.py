import sys

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()  # dummy node
        self.tail = self.head  # maintain tail pointer for fast end insert
        self.cursor = self.head  # insertion happens after cursor

    def insert(self, ch):
        new_node = Node(ch)
        new_node.next = self.cursor.next
        self.cursor.next = new_node

        # If we inserted at end, update tail
        if self.cursor == self.tail:
            self.tail = new_node

        # Move cursor to new node
        self.cursor = new_node

    def move_to_start(self):
        self.cursor = self.head

    def move_to_end(self):
        self.cursor = self.tail

    def get_string(self):
        result = []
        current = self.head.next
        while current:
            result.append(current.data)
            current = current.next
        return ''.join(result)

# Read from stdin until EOF
while True:
    text = input()
    if not text:
        break
    ll = LinkedList()

    for ch in text:
        if ch == '[':
            ll.move_to_start()
        elif ch == ']':
            ll.move_to_end()
        else:
            ll.insert(ch)

    print(ll.get_string())
