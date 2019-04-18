"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place."""

array = [3, 4,-1, 1]


def findlowestpos(array):
	sortedarray = sorted(array)
	i=0 #default value if no positive integers in entire array
	print(sortedarray)
	for elem in sortedarray:
		if elem >=0:
			x= elem
			i = sortedarray.index(elem)
			break

	while (i+1) != len(sortedarray) and sortedarray[i] +1 == sortedarray[i+1]:
		i += 1

	return (sortedarray[i]+1)


print(findlowestpos(array))
print(findlowestpos([1,2,0]))
