# cook your dish here
for _ in range(int(input())):
    n,x=map(int,input().split())
    earn=pow(2,x)
    print(earn//pow(2,n))