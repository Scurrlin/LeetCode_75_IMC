# Search in Rotated Sorted Array

def search(self, nums: List[int], target: int) -> int:

# This line defines a function named `search`. The function takes three
# parameters: `self`, `nums`, and `target`. `self` is typically used in the
# context of class methods, but here it seems unnecessary as the function isn't
# part of a class. `nums` is expected to be a list of integers and `target` is
# an integer. The function is expected to return an integer.

    if not nums:
        return -1

# If the list `nums` is empty, the function returns -1. This is a base case.

    start, end = 0, len(nums) - 1

# This line initializes two variables, `start` and `end`, to the first and last
# indices of `nums`, respectively. These variables will be used to perform a
# binary search.

    while start <= end:

# This line starts a while loop that continues as long as `start` is less than
# or equal to `end`.

        mid = (start + end) // 2

# This line calculates the middle index of the current search range.

        if nums[mid] == target:
            return mid
# If the element at the middle index is equal to the target, the function
# returns the middle index. This means the target has been found.

        if nums[start] <= nums[mid]:

# If the element at the start index is less than or equal to the element at the
# middle index, it means the left half of the array is sorted.

            if nums[start] <= target <= nums[mid]:
                end = mid - 1

# If the target is between the start and middle elements, it means the target is
# in the sorted part of the array. So, the function updates `end` to `mid - 1`
# to search in the left half.

            else:
                start = mid + 1

# Otherwise, the function updates `start` to `mid + 1` to search in the right
# half.

        else:

# If the element at the start index is greater than the element at the middle
# index, it means the right half of the array is sorted.

            if nums[mid] <= target <= nums[end]:
                start = mid + 1

# If the target is between the middle and end elements, it means the target is
# in the sorted part of the array. So, the function updates `start` to `mid + 1`
# to search in the right half.

            else:
                end = mid - 1

# Otherwise, the function updates `end` to `mid - 1` to search in the left half.

    return -1

# If the while loop finishes without finding the target, the function returns
# -1. This means the target is not in the array.