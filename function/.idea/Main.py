
class Node:
    def __init__(self, x, next):
        self.val = x
        self.next = next
one = Node(1, None)
two = Node(2, None)
three = Node(3, None)
four = Node(4, None)
five = Node(5, two)

one.next = five
two.next = three
three.next = four
four.next = None

pointer = one
while pointer is not None:
    print(pointer.val)
    pointer = pointer.next

def length(x):
    n = 0
    while x is not None:
        n = n + 1
        x = x.next
    return n
print("length: ", length(one))