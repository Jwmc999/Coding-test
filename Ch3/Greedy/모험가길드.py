n = int(input())
data = list(map(int, input().split()))
data.sort()

# number of total groups
result = 0
# number of adventurers in current group
count = 0

# check fear score from the lowest
for i in data:
	# include the adventurer
	count += 1
	# compose a new group if number of adventurers >= current fear score
	if count >= i:
		# number of total groups increased
		result += 1
		# initialize the number of adventurers in the current group
		count = 0
		
print(result)
