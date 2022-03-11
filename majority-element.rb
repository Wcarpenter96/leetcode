# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    ct = Hash.new {|hash, key| hash[key] = 0}
    for num in nums
        ct[num] += 1
    end
    ct.invert.max.last
end

# @param {Integer[]} nums
# @return {Integer}
def majority_element(nums)
    nums.tally.invert.max.last
end