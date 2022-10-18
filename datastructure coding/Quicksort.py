def partition(a,si,ei):




def Quick_sort(a,si,ei):
    if si >= ei:
        return
    pivot = partition(a,si,ei)
    Quick_sort(a,si,pivot-1)
    Quick_sort(a,pivot+1,ei)




a = [9,8,7,1,2,4,3,5]
print(Quick_sort(a,0,8))