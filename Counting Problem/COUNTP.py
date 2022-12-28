# cook your dish here
for _ in range(int(input())):
    n=int(input())
    A=list(map(int,input().split()))
    c=0
    for i in A:
        if(i%2==1):
            c+=1
    if c%2==0 and c>0:
        print("YES")
    else:
        print("NO")