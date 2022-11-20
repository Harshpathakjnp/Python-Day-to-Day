class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def printtree(root):
    if root == None:
        return
    print("Root -", root.data, end=':')
    if root.left != None:
        print("Left -", root.left.data, end=',')
    if root.right != None:
        print("Right -", root.right.data, end='')
    print()
    printtree(root.left)
    printtree(root.right)


def treeinput():
    rootdata = int(input())
    if rootdata == -1:
        return None
    root = BinaryTreeNode(rootdata)
    lefttree = treeinput()
    righttree = treeinput()
    root.left = lefttree
    root.right = righttree
    return root


def numnodes(root):
    if root == None:
        return 0
    leftcount = numnodes(root.left)
    rightcount = numnodes(root.right)
    return 1 + leftcount + rightcount


def findlargest(root):
    if root == None:
        return -1
    leftlargest = findlargest(root.left)
    rgtlargest = findlargest(root.right)
    maxm = max(root.data, leftlargest, rgtlargest)
    return maxm


def numleafnodes(root):
    if root == None:
        return 0
    if root.left == None and root.right == None:
        return 1
    numleafleft = numleafnodes(root.left)
    numleafright = numleafnodes(root.right)
    return numleafright + numleafleft


def printdepthk(root, k):
    if root == None:
        return
    if k == 0:
        print(root.data)
        return
    printdepthk(root.left, k - 1)
    printdepthk(root.right, k - 1)


def removeleaf(root):
    if root == None:
        return None
    if root.left == None and root.right == None:
        return None
    root.left = removeleaf(root.left)
    root.right = removeleaf(root.right)
    return root


def isBalanced(root):
    if root == None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if lh > 1 or rh > 1:
        return False
    isleftBalanced = isBalanced(root.left)
    isrightBalanced = isBalanced(root.right)
    if isrightBalanced and isleftBalanced:
        return True
    else:
        return False


def height(root):
    if root == None:
        return 0
    return 1 + max(height(root.left), height(root.right))


btn = treeinput()
printtree(btn)
# print(numNodes(btn))
# print(findlargest(btn))
print("Number of Leaf Nodes =", numleafnodes(btn))
# btn = removeleaf(btn)
# printtree(btn)
s = isBalanced(btn)
print(s)
