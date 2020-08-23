num=list(range(int(input())))
b=[]
for i in num:
    a=input()
    b.append(a)
for i in set(b):
    print(i+':'+str(b.count(i)))
