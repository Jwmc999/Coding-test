# receive N, K
n, k = map(int, input().split())
# Receive all elements of array A
a = list(map(int, input().split()))
# Receive all elements of array B
b = list(map(int, input().split()))

# array A: ascending sort
a.sort()
# array B: descending sort
b.sort(reverse=True)

# Compare elements of A and B at maximum Kth round
for i in range(k):
  # if element of A < element of B
  if a[i] < b[i]:
    # swap two elements
    a[i], b[i] = b[i], a[i]
  # if element of A >= element of B
  else:
    break
    
print(sum(a))
