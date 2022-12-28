# cook your dish here
for _ in range(int(input())):
    n,x,c=map(int,input().split())
    ar=list(map(int,input().split()))
    sum=0
    for i in ar:
        if i<(x-c):
            sum+=x-c
        else:
            sum+=i
    print(sum)