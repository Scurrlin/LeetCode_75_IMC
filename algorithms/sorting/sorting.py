# Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Last i elements are already in place, so we don't need to check them
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Define the array to be sorted
arr = []
# Call the bubble_sort() function with the array as an argument
bubble_sort(arr)
# Now the 'arr' variable holds the sorted array
print("Sorted array:", arr)

# Insertion Sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]  # Current element to be compared
        j = i - 1     # Index of the previous element
        
        # Move elements of arr[0..i-1], that are greater than key, to one
        # position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = []
insertion_sort(arr)
print("Sorted array:", arr)

# Selection Sort

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

arr = []
selection_sort(arr)
print("Sorted array:", arr)

# Merge Sort

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        left_half = arr[:mid]  # Divide the array into two halves
        right_half = arr[mid:]

        # Recursive call on each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

arr = []
selection_sort(arr)
print("Sorted array:", arr)

# Quick Sort

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        
        # Recursively sort elements before and after the pivot
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Select the pivot element (rightmost element)
    i = low - 1  # Index of the smaller element
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap arr[i+1] and arr[high] (put pivot element in the correct position)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

arr =[]
# Call the quick_sort() function with the array and the range of indices as arguments
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)