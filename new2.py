def numberOfTokens(expiryLimit, commands):
    # Write your code here
    i=0
    hash1={}
    count=0
    while i<len(commands):
        if commands[i][0]==0:
            temp1=commands[i][1]
            hash1[temp1]=commands[i][2]+expiryLimit
        else:
            if commands[i][1] in hash1:
                if commands[i][2]<=hash1[commands[i][1]]:
                    temp2=commands[i][1]
                    hash1[temp2]=commands[i][2]+expiryLimit
        i=i+1
    for i in hash1:
        if hash1[i]>commands[-1][2]:
            count+=1
    return count

'''def numberOfTokens(expiryLimit, commands):
    # Write your code here
    i=0
    hash1={}
    count=0
    while i<len(commands):
        if commands[i][0]==0:
            temp1=commands[i][1]
            hash1[temp1]=commands[i][2]+expiryLimit
            continue
        if commands[i][1] not in hash1:
            continue
        if commands[i][2]<=hash1[commands[i][1]]:
                temp2=commands[i][1]
                hash1[temp2]=commands[i][2]+expiryLimit
        i=i+1
    for i in hash1:
        if hash1[i]>commands[-1][2]:
            count+=1
    return count'''

numberOfTokens(8192,[[1, 23937, 405],
[1, 2755, 643],
[0, 21230, 1474],
[1, 21230,1609],
[0, 24942, 2453],
[0, 15143, 2839],
[0, 18242,3321],
[1, 24942, 3709],
[0, 6123, 4310],
[1, 18242, 5031]])