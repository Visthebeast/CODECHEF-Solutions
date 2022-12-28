# cook your dish here
def min_steps(AA, BB, K):
  distance = abs(AA - BB)
  steps = (distance + K - 1) // K
  return steps

for i in range(int(input())):
    AA,BB,K=map(int,input().split())
    steps = min_steps(AA, BB, K)

    print(steps)
