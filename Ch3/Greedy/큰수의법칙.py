# Input of N, M, K
n, m, k = map(int, input().split())
# Integer input of N length
data = list(map(int, input().split()))

# sort input
data.sort()
# largest integer
first = data[n-1]
# second largest integer
second = data[n-2]

# count how many times the largest integer is added
count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
# add the largest integer
result += (count) * first
# add the second largest integer
result += (m - count) * second

# final result
print(result)
