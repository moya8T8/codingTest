#백준 2501번 약수구하기 
N, K = map(int, input().split())  
c = []
for i in range(1,N+1):
    if(N%i==0):
      c.append(i)

if K > len(c):
    print(0)
else:
    print(c[K-1])