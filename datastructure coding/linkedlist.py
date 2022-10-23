class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printll(head1):
    while head1 != None:
        print(head1.data, end=" -> ")
        head1 = head1.next
    print("None")


def length(head):
    count = 0
    while head is not None:
        count += 1
        head = head.next
    return count

def insertatIR(head,i,data):
    if i==0:
        newNode = Node(data)
        newNode.next = head
        return newNode
    if head is None:
        return None
    smallHead = insertatIR(head.next,i-1,data)
    head.next = smallHead
    return head


def insertatI(head, i, data):
    if i < 0 or i > length(head):
        return head
    count = 0
    prev = None
    curr = head
    while count < i:
        count += 1
        prev = curr
        curr = curr.next
    newNode = Node(data)
    if prev is not None:
        prev.next = newNode
    else:
        head = newNode
        head.next = curr
    newNode.next = curr

    return head


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
insertatIR(head1, 2, 9)
printll(head1)
printll(insertatIR(head1, 0, 11))
