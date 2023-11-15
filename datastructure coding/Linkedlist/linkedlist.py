class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printall(head):
    while head != None:
        print(str(head.data) + " ->", end=" ")
        head = head.next
    print("None")
    return


# def reverselist1(head):
#     if head is None or head.next is None:
#         return head
#     smallhead = reverselist1(head.next)
#     curr = smallhead
#     while curr.next is not None:
#         curr = curr.next
#     curr.next = head
#     head.next = None
#     return smallhead
def reverselist2(head):
    if head is None or head.next is None:
        return head
    smallhead = reverselist2(head.next)
    tail = head.next
    tail.next = head
    head.next = None
    return smallhead



# def takeinput():
#     inputList = [int(ele) for ele in input().split()]
#     head = None
#     for currdata in inputList:
#         if currdata == -1:
#             break
#         newNode = Node(currdata)
#         if head is None:
#             head = newNode
#         else:
#             curr = head
#             while curr.next is not None:
#                 curr = curr.next
#             curr.next = newNode
#     return head

def takeinputs():
    head = None
    inputlist = [int(ele) for ele in input().split()]
    for currdata in inputlist:
        if currdata == -1:
            break
        newNode = Node(currdata)
        if head is None:
            head = newNode
            curr = newNode
        else:
            curr.next = newNode
            curr = newNode
    return head
def insertAtI(head,d,pos):
    count = 0
    curr = head
    prev = None
    newNode = Node(d)
    while count < pos:
        count += 1
        prev = curr
        curr = curr.next
    prev.next = newNode
    newNode.next = curr


    return head


h = takeinputs()
printall(h)
p = reverselist2(h)
printall(p)

