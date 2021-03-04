# the minimum cost to reduce an array
# cost = sum of numbers being removed
# Given an array consisting of N integers, find the minimum cost to reduce the 
# given array to a single element by choosing any pair of consecutive array 
# elements and replacing them by (array[i] + array[i+1]) 

#cheapest(array, counter, othercounter) produces the minimum cost given the array
def cheapest(array, counter, othercounter):
    if (counter >= othercounter): 
        return 0; 
    cost = 100000000000000
    for index in range(counter, othercounter):  
        RS = cheapest(array, index + 1, othercounter) 		
        LS = cheapest(array, counter, index) 
        cost = min(cost, LS + RS + Combine(array, counter, othercounter))
    return cost 

#Combine(array, counter, othercounter) 
def Combine(array, counter, othercounter):     
	sum = 0 
	for l in range(counter, othercounter + 1): 
		sum += array[l] 
	return sum 

# main(array) produces the minimum cost and is the driver function
def main(myarray): 
	n = len(myarray) 
	array = myarray 
	print(cheapest(array, 0, n - 1))

#TESTS
main([0, 0, 0, 0]) #0
main([1, 2, 3, 4]) #19
main([5, -2, 16, 10, 30, -13]) #112
main([-2,-5,-10,-3]) #-53
main([1, 1, 1, 1]) #8
main([1, -1, 1, -1]) #-1



