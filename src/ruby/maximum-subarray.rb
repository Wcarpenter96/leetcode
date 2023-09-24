# @param {Integer[]} nums
# @return {Integer}

def max_sub_array(nums)
    sum = nums[0]
    max_sum = nums[0]
    
    nums.each_with_index do |num, i|
        if i == 0 then next end
        sum = [num, sum + num].max
        max_sum = [max_sum, sum].max
    end
    
    max_sum
end