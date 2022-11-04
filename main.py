# Python3 program to
# sort array using
# pancake sort


# Reverses arr[0..i] */
def flip(arr, i):
  start = 0
  for x in range(i+1):
    # using Tilde operator(~)
    arr[x] = -arr[x]

  while start < i:
    temp = arr[start]
    arr[start] = arr[i]
    arr[i] = temp
    start += 1
    i -= 1


# Returns index of the maximum
# element in arr[0..n-1] */
def findMax(arr, n):
  mi = 0
  for i in range(0, n):
    if arr[i] > arr[mi]:
      mi = i
  return mi



# The main function that
# sorts given array
# using flip operations
def pancakeSort(arr, n):

  # Start from the complete
  # array and one by one
  # reduce current size
  # by one
  curr_size = n-1
  
  #Find Max
  #Flip @ max's index
  #If max is positive, Flip
  #Flip Max to correct spot at end
  #increment end cursor
  
  while curr_size > -1:
  
    absArr = np.absolute(arr)
    absArr = absArr[0:curr_size+1]
    
    index_max = np.argmax(absArr)
  
    
    flip(arr,index_max)
    
    print("Flip @ Max")
    print(arr)
    if arr[0] > 0:
      print("Invert:")
      flip(arr,0)
      print(arr)
      
    print("Flip to cursor")
    flip(arr,curr_size)
    curr_size-=1
    print(arr)
    
    


# A utility function to
# print an array of size n
def printArray(arr, n):
  for i in range(0, n):
    print("%d" % (arr[i]), end=" ")
  print("\n")


# Driver program
import numpy as np

negaArr = np.array([-3, 2, 4, -1, -5])
n = len(negaArr)
printArray(negaArr, n)
pancakeSort(negaArr, n)

# This code is contributed by shreyanshi_arun.
