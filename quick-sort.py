import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def quickSort(arr):
     quickSortH(arr,0,len(arr)-1)
     return arr

def quickSortH(arr,i,j):
    if i < j:
        loc = partition(arr, i, j)
        quickSortH(arr, i, loc-1)
        quickSortH(arr, loc+1, j)

def partition(arr, i, j):
    pivot = arr[i]
    low = i
    high = j
    while low <= high:
        while low <= high and arr[low] <= pivot:
            low += 1
        while high >= low and arr[high] > pivot:
            high -= 1
        if low < high:
            arr[low], arr[high] = arr[high], arr[low]
    arr[i], arr[high] = arr[high], arr[i]
    return high

   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()


