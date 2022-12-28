# cook your dish here
for _ in range(int(input())):
    n=int(input())
    e=[]
    c=0
    u=[]
    flag=0
    A=list(map(int,input().split()))
    for i in range(0,n):
        if i==n-1:
            if A[i] in u:
                print("NO")
                flag=1
                break
            c+=1
            u.append(A[i])
            e.append(c)
        elif A[i]==A[i+1]:
            c+=1
        elif A[i]!=A[i+1]:
            if A[i] in u:
                print("NO")
                flag=1
                break
            c+=1
            e.append(c)
            u.append(A[i])
            c=0
    myset=set(e)
    if len(myset)!=len(e) and flag!=1:
        print("NO")
    elif flag!=1:
        print("YES")
        