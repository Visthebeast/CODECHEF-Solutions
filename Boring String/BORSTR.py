# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    l=list(s)
    c=0
    u=[]
    w=[]
    y=""
    for i in range(0,n):
        if i==n-1:
            c+=1
            y+=l[i]
            u.append(c)
            w.append(y)
        elif l[i]==l[i+1]:
            c+=1
            y+=l[i]
        else:
            c+=1
            y+=l[i]
            u.append(c)
            w.append(y)
            c=0
            y=""
    ma=0
    '''for i in u:
        if i>1:
            if i-1>ma:
                ma=i-1'''
    ma=max(u)-1
    #print(u)
    #print(w)
    #print(ma)
    uniq=[0]
    flag=0
    
    for i in range(0,len(w)):
        for j in range(i+1,len(w)):
            if w[i]==w[j]:
                uniq.append(u[j])
                flag=1
   # print(uniq)
    #print(ma)
    #print(max(uniq))
#    print(flag)
    if flag!=1 and ma==0:
        print(0)
    elif max(uniq)>ma:
        print(max(uniq))
    else:
        print(ma)
            
            