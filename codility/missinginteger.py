def solution(A):
    sortednumbers = sorted(A) #array of numbers is sorted using a built-in python function
    counter = 1               #using a counter starting at 1, it's important that this is defined outside of the for loop (otherwise function will only return 2)
    for i in sortednumbers:   #iterating through the lsit of sorted numbers
        if i == counter:      #if i == counter (the number is in the list, 1 is added to the counter and the for loop continues iterating)
            counter += 1
        if i > counter:       # if i > counter, that means that the counter is not found in the list, thus the for loop is broken using break
            break
    return counter            #at the end of the program, coutner is returned. If the missing integer was not in the list, the break took care of 
                              # returning that number, since counter was defined otuside of the loop. If the number was larger, e.g 4 in A= [1, 2, 3], 
                              # the break also took care of it


print(solution([1, 2, 5]))
