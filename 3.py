n=int(input())
ans=[]
i=1
while len(ans)<n:
    a=list(map(int, str(i)))
    if 3 not in a and 4 not in a and 7 not in a:
        ans.append(i)
    i+=1
print(ans[n-1])