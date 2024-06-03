# 3 Sum

def threeSum(self, nums: List[int]) -> List[List[int]]:

# This line defines a function named `threeSum`. The function takes two
# parameters: `self` and `nums`. `self` is typically used in the context of
# class methods, but here it seems unnecessary as the function isn't part of a
# class. `nums` is expected to be a list of integers. The function is expected
# to return a list of lists of integers.

    nums.sort()

# This line sorts the list `nums` in ascending order.

    res = []

# This line initializes an empty list `res` that will store the result.

    for i in range(len(nums) - 2):

# This line starts a for loop that iterates from 0 to `len(nums) - 3`. For each
# iteration, the current index is stored in the `i` variable.

        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
# If the current number is the same as the previous number, the loop continues
# to the next iteration. This is to avoid duplicate results.

        left, right = i + 1, len(nums) - 1

# This line initializes two variables, `left` and `right`, to the next index
# after `i` and the last index of `nums`, respectively. These variables will be
# used to perform a two-pointer search.

        while left < right:

# This line starts a while loop that continues as long as `left` is less than
# `right`.

            total = nums[i] + nums[left] + nums[right]

# This line calculates the sum of the numbers at the `i`, `left`, and `right`
# indices and stores it in `total`.

            if total < 0:
                left += 1

# If `total` is less than 0, the function increments `left` by 1 to increase the
# sum.

            elif total > 0:
                right -= 1

# If `total` is greater than 0, the function decrements `right` by 1 to decrease
# the sum.

            else:
                res.append([nums[i], nums[left], nums[right]])

# If `total` is equal to 0, the function appends the numbers at the `i`, `left`,
# and `right` indices to `res`.

                while left < right and nums[left] == nums[left + 1]:
                    left += 1

# While `left` is less than `right` and the next number is the same as the
# current number, the function increments `left` by 1. This is to avoid
# duplicate results.

                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

# While `left` is less than `right` and the previous number is the same as the
# current number, the function decrements `right` by 1. This is to avoid
# duplicate results.

                left += 1
                right -= 1

# After finding a valid triplet, the function increments `left` by 1 and
# decrements `right` by 1 to continue the search.

    return res

# After the loop has finished, this line returns the result. If no three numbers
# sum to zero, `res` will be an empty list.