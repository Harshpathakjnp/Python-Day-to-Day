def Binary_search(a,x,si,li):
    if si>li:
        return -1
    mid = (si + li)//2
    if a[mid]== x:
        return mid
    elif a[mid]>x:
        return Binary_search(a,x,si,mid-1)
    else:
        return Binary_search(a,x,mid+1,li)

a = [1,2,4,6,8,9]
p = Binary_search(a,2,0,5)
print(p)