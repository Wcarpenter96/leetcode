# @param {Integer[]} nums
# @param {Integer} k
# @return {Boolean}
def contains_nearby_duplicate(nums, k)
  h = {}
  nums.each_with_index do |num, i|
    unless h[num].nil?
      if i-h[num] <= k
        return true
      else
        h[num] = i
      end
    else
      h[num] = i
    end
  end
  false
end