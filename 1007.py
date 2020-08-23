month=12


def avg(money):
    sum=0
    for m in money:
        sum=sum+m
    return round(sum/12,2)








monthlist=[]
for i in list(range(month)):
    monthlist.append(input())
print('$'+str(avg(monthlist)),end='')
    
