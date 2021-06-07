#Bubble sort
def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n-1):
        for j in range(0, n-1-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
arr = [33,44,55,77,22]
bubbleSort(arr)

for i in range(len(arr)):
    print(arr[i])