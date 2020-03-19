a=int(input())
b=int(input())
if (a>1000 & b!=1) | (a>1000 & b==1 & a//1000==a%10 & a//(a//100)==a%(a%100) ):
    print("YES")
else:
    print("NO")