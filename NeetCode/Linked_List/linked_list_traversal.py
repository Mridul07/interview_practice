class Node():
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Linked_List():
    def __init__(self) -> None:
        pass


def print_ll(head):
    
    while head:
        print(f'{head.val} ')
        head = head.next

def create_ll_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    
    return res

def sum_ll(head):
    sum = 0
    while head:
        sum += head.val
        head = head.next
    
    return sum

def find_target_ll(head, target):

    while head:
        if head.val == target:
            return True
        head = head.next
    
    return False

def get_node_at_index(head, ind):

    for i in range(ind):
        if not head:
            return None
        head = head.next
    
    return head.val

def reverse_ll(head):
    prev = None
    curr = head
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    
    return prev

def zip_ll(head1, head2):
    tail = head1
    curr1 = head1.next
    curr2 = head2
    count = 0

    print(f'Head 1 val: {head1.val}')
    print(f'Head 2 val: {head2.val}')

    while curr1 and curr2:

        print(f'Curr 1 val: {curr1.val}')
        print(f'Curr 2 val: {curr2.val}')
        if count % 2 == 0:
            print(f'Curr 2 val inside if: {curr2.val}')
            tail.next = curr2
            curr2 = curr2.next
        else:
            print(f'Curr 1 val inside if: {curr1.val}')
            tail.next = curr1
            curr1 = curr1.next
        tail = tail.next
        count += 1
    
    if curr1: tail.next = curr1
    if curr2: tail.next = curr2
    
    print(f'Printing head at the end {head1.val}')
    return head1

# Creating the Linked List nodes
# First 5 are members of list 1 and next 2 are for list 2
node1 = Node(5)
node2 = Node(4)
node3 = Node(3)
node4 = Node(7)
node5 = Node(6)

node6 = Node(10)
node7 = Node(11)

# Linking the list 1 with node1 as the head
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Linking the list2 with node6 as the head
node6.next = node7

# print_ll(node1)

# print(create_ll_array(node1))

# print(sum_ll(node1))

# print(find_target_ll(node1, 41))

# print(get_node_at_index(node1, 1))

# print_ll(node1)
# print("Now reversing the list:")
# reverse_ll(node1)
# print_ll(node5)

print_ll(node1)
print("------------------")
print_ll(node6)
print("------------------")
zip_ll(node6, node1)
print_ll(node6)