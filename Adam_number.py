n1=int(input())
res1=0
res2=0
s1=n1*n1;
while(n1>0):
       r1=n1%10
       res1=res1*10+r1
       n1=n1//10
s2=res1*res1;
while(s2>0):
       r2=s2%10
       res2=res2*10+r2
       s2=s2//10
if(s1==res2):
 print("True");
else:
 print("False");
