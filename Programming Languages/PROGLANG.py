# cook your dish here
for i in range(int(input())):
    (a,b,a1,b1,a2,b2)=map(int,input().split())
    if(a==a1 or a==b1) and (b==a1 or b==b1):
        print("1")
        continue
    elif(a==a2 or a==b2) and (b==a2 or b==b2):
        print("2")
        continue
    else:
        print("0")