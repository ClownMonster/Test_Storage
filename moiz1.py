

min = 9999999999
max = 0
data = []

def find_min_max():
	global data, min, max
	for i in data:
		if i <= min:
			min = i
		elif i >= max:
			max = i 
		else:
			continue
	return


if __name__ == '__main__':
	size = int(input("Enter the size of the array : "))
	print("Enter the element of array : ")
	for i in range(size):
		data.append(int(input()))
	print(data)

	find_min_max()

	print(f'min: {min} and index of min : {data.index(min)}')
	print(f'max: {max} and index of max : {data.index(max)}')
	



