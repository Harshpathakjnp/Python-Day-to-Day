# a = {"abc":123 , "a":5 , 12345:"qwert"}
# a['tu'] = 123
# for i in a:
#     print(i,a[i])
# a.pop('tu')
# print(a)
sent = "this is word having many many word"
words = sent.split()
d = {}
for i in words:
    d[i]=d.get(i,0)+1
print(d)