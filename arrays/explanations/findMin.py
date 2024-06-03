# Find Minimum in Rotated Sorted Array

def findMin(self, nums: List[int]) -> int:

# This line defines a function named `findMin`. The function takes two
# parameters: `self` and `nums`. `self` is typically used in the context of
# class methods, but here it seems unnecessary as the function isn't part of a
# class. `nums` is expected to be a list of integers. The function is expected
# to return an integer.

    if len(nums) == 1:
        return nums[0]

# If the list `nums` contains only one element, the function returns that
# element.

    if nums[0] < nums[-1]:
        return nums[0]

# If the first element of `nums` is less than the last element, the function
# returns the first element. This is based on the assumption that `nums` is a
# rotated sorted list, so if the first element is less than the last one, the
# list is already sorted and the first element is the smallest.

    left, right = 0, len(nums) - 1

# This line initializes two variables, `left` and `right`, to the first and last
# indices of `nums`, respectively. These variables will be used to perform a
# binary search.

    while left <= right:

# This line starts a while loop that continues as long as `left` is less than or
# equal to `right`.

        mid = (left + right) // 2

# This line calculates the middle index of the current search range.

        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

# If the element at the middle index is greater than the next element, the
# function returns the next element. This is because in a rotated sorted list,
# the pivot point is the only place where the next number is smaller than the
# current number.

        if nums[mid] < nums[mid - 1]:
            return nums[mid]

# If the element at the middle index is less than the previous element, the
# function returns the current element. This is because in a rotated sorted
# list, the pivot point is the only place where the previous number is larger
# than the current number.

        if nums[mid] > nums[0]:
            left = mid + 1

# If the element at the middle index is greater than the first element, the
# function updates `left` to `mid + 1`. This is because the minimum value must
# be to the right of `mid`.

        else:
            right = mid - 1

# Otherwise, the function updates `right` to `mid - 1`. This is because the
# minimum value must be to the left of `mid`.
