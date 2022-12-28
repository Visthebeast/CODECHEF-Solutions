# cook your dish here
for _ in range(int(input())):
    a,c=map(int,input().split())
    if (c-a)%2==0:
       d=(c-a)//2
       print(a+d)
    else:
        print(-1)
        