def transnum(a):
    a=a.replace('A','2')
    a=a.replace('B','2')
    a=a.replace('C','2')
    a=a.replace('D','3')
    a=a.replace('E','3')
    a=a.replace('F','3')
    a=a.replace('G','4')
    a=a.replace('H','4')
    a=a.replace('I','4')
    a=a.replace('J','5')
    a=a.replace('K','5')
    a=a.replace('L','5')
    a=a.replace('M','6')
    a=a.replace('N','6')
    a=a.replace('O','6')
    a=a.replace('P','7')
    a=a.replace('R','7')
    a=a.replace('S','7')
    a=a.replace('T','8')
    a=a.replace('U','8')
    a=a.replace('V','8')
    a=a.replace('W','9')
    a=a.replace('X','9')
    a=a.replace('Y','9')
    a=a.replace('-','')
    standardphone=a[:3]+'-'+a[3:]
    return standardphone


num=list(range(int(input())))
b=[]
for n in num:
    c = input()
    b.append(c)
d={}
for a in b:
    standard=transnum(a)
    if None==d.get(standard):
        d[standard]=1
    else:
        d[standard]=d[standard]+1
d=sorted(d.items())
for key,value in d.items():
    if value >1:
        print(key+':'+str(value))

