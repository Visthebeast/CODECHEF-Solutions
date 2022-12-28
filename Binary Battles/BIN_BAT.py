# cook your dish here
for i in range(int(input())):
    (n,a,b)=map(int,input().split())
    t=n
    c=0
    while(t!=1):
        t/=2
        c+=1
  #  print(c)
    time=c*a
    time+=(c-1)*b
    print(time)