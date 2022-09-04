#3460번 백준 문제구하기 

T = int(input())
for _ in range(T):
  n = bin(int(input())).split('0b')[1]
  for i in range(len(n)):
    if(n[-i-1] == '1'):
      print(i, end=' ')