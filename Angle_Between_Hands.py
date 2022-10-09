h,m=map(int,input().split(':'))
def angle(h,m):
    if h==12:
        h=0
    if m==60:
        m=0;
        h=h+1
        if h>12:
            h=h-12
    ha=(h*60+m)*0.5
    ma=6*m
    ang=abs(ha-ma)
    ang=min(360-ang,ang)
    return ang
print(angle(h,m))    