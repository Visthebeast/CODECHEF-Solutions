# cook your dish here
for _ in range(int(input())):
    n,k=map(int,input().split())
    A=list(map(int,input().split()))
    for i in A:
        if(k>=i):
            print(1,end="")
            k-=i
        else:
            print(0,end="")
    print("")
    