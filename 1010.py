import sys
a,b=input().split()
lista=[a,b]
for line in sys.stdin.readlines(lista):
    if not line:
        break
    else:
        print(int(a)+int(b))
'''
a,b=input().split()
print(int(a)+int(b))
'''
