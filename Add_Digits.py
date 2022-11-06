n = int(input()) 
s = sum(int(i) for i in str(n)) 
print(s%9if s%9 else 9) 