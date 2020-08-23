new = ["flower", "flow", "flight"]
h = 0
new_len = (len(new)-1)
while h < new_len:
    if len(new[h]) > len(new[h+1]):
        ind_ex = h+1
    else:
        ind_ex = h
    h = h+1
j = 0
prefix = ""
flag=False
while j < len(new[ind_ex]):
    i = 1
    while i <= new_len:
        if new[0][j] == new[i][j]:
            i = i+1
        else:
            print(prefix)
            flag=True
            break
    if flag:
        break
    prefix += new[0][j]
    j = j+1
if not flag:
    print(prefix)
