#3460번 백준 문제구하기 

T = int(input())
for _ in range(T):
  n = bin(int(input())).split('0b')[1]
  for i in range(len(n)):
    if(n[-i-1] == '1'):
      print(i, end=' ')

      #T와 N을 미리 정하고 시작하는 거 좋은 방법인거 같습니다 