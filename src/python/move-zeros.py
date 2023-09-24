from re import template


nums = [0,1,0,3,12]


def moveZeroes(nums) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # Pointers
    i = 0
    j = 1
    while j < len(nums):
        if nums[i] == 0 and nums[j] == 0:
            j += 1
        elif nums[i] == 0 and nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif nums[i] != 0:
            i += 1
            j += 1
nums = [4,2,4,0,0,3,0,5,1,0]
moveZeroes(nums)
print(nums)

