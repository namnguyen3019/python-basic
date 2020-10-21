class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

zero = Node()
one = Node(1, None)
two = Node(2, None)
three = Node(3, None)
zero.next = one
one.next = two
two.next = three

head = zero
pointer = head
print(head) # Print the address

while pointer:
    print(pointer.value)
    pointer = pointer.next



