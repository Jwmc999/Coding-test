data = input()
# convert all to 0
count0 = 0
# convert all to 1
count1 = 0

# the first element 
if data[0] == '1':
	count0 += 1
else:
	count1 += 1
	
# check all elements from the second element
for i in range(len(data) - 1):
	if data[i] != data[i+1]:
		# if the next element changes to 1
		if data[i+1] == '1':
			count0 += 1
		# if the next element changes to 0
		else:
			count1 += 1

print(min(count0, count1))
