import math

n = 5
x = 2
sum = 0
for i in range(n):
  term = (-1)**i * (x**(2*i))/math.factorial(2*i)
  sum += term

print(sum)