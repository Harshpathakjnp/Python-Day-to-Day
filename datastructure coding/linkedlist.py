class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

def printll(head1):
    while head1 != None:
        print(head1.data, end=" -> ")
        head1 = head1.next
    print("None")
def takeinput():
    inputlist = [int(ele) for ele in input().split()]
    head = None
    tail = None
    for currdata in inputlist:
        if currdata == -1:
            break
        newNode = Node(currdata)
        if head is None:
            head = newNode
            tail = newNode
        else:
            tail.next = newNode
            tail = newNode

    return head


head1 = takeinput()
printll(head1)
