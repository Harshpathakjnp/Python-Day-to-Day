
def push(st,item):
    st.append(item)
    print(st)

def pops(st):
    st.pop()
    print(st)




st = []
n = 1
while n != 0:
    n = int(input("Enter Your Choice : 1-> Push    2 -> Pop  0-> Exit"))
    if n == 0:
        exit()
    elif n == 1:
        item = int(input("Enter Number to Push"))
        push(st,item)
    elif n == 2:
        pops(st)
