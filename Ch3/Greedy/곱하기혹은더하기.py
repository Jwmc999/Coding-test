data = input()

# convert the first char to int
result = int(data[0])

for i in range(1, len(data)):
	# if 0 or 1, conduct plus
	num = int(data[i])
	if num <= 1 or result <=1:
		result += num
	else:
		result *= num
		
print(result)
