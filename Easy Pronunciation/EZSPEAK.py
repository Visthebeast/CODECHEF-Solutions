# cook your dish here
import string
for _ in range(int(input())):
    co=list(string.ascii_lowercase)
    vow=['a','e','i','o','u']
    for i in co:
        if i in vow:
            co.remove(i)
    n=int(input())
    s=input()
    li=list(s)
    c=0
    for i in li:
        if c>=4:
            break
        elif i in co:
            c+=1
        else:
            c=0
    if c>=4:
        print("NO")
    else:
        print("YES")