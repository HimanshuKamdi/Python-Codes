# ar=eval(input("Enter elements of list:  "))
ar=[6,5,4,3,2]

#Selection Sort
def selectionsort(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):        
            if array[j] < array[min_idx]:
                min_idx = j
        (array[i], array[min_idx]) = (array[min_idx], array[i])
    print("List after Selection Sort: ",array)
selectionsort(ar)


#Bubble Sort
def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j],array[j+1] = array[j+1],array[j]
    print("List after Bubble Sort: ",array)

#Insertion Sort
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key
    print("List after Insertion Sort: ",array)


# bubbleSort(ar)
insertionSort(ar)   

for i in range(1,len(ar)):
    key=ar[i]
    j=i-1
    while j>=0 and key<ar[j]:
        ar[j+1]=ar[j]
        j=j-1
    ar[j+1]=key 

for i in range(len(ar)):
    min_ind=i
    for j in range(i+1,len(ar)):
        if ar[j]<ar[min_ind]:  
            min_ind=j
    ar[min_ind],ar[i]=ar[i],ar[min_ind]  

for i in range(len(ar)):
    for j in range(len(ar)-i-1):
        if ar[j]>ar[j+1]:
            ar[j],ar[j+1]=ar[j+1],ar[j]
