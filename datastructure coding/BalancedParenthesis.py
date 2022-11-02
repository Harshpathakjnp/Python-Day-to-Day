def isBalanced(parenthesis):
    s = []
    for char in parenthesis:
        if char in "[{(":
            s.append(char)
        elif char is ")":
            if (not s or s[-1]!="("):
                return False
            s.pop()
        elif char is "}":
            if (not s or s[-1]!="{"):
                return False
            s.pop()
        elif char is "]":
            if (not s or s[-1]!="["):
                return False
            s.pop()
    if len(s)==0:
        return True
    else:
        return False



parenthesis = input()
ans = isBalanced(parenthesis)
print(ans)