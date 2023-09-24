# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer}
def search_insert(nums, target)
    max = nums.length - 1
    min = 0
    while min <= max
        i = (max+min)/2
        if nums[i] == target
            return i
        elsif nums[i] < target
            min = i + 1
        else
            max = i - 1
        end 
    end
    min
end

nums = [1,3,5,6]
target = 5
puts search_insert(nums, target)