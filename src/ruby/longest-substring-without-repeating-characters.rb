# @param {String} s
# @return {Integer}
def length_of_longest_substring(s)
  #  i is beginning of substring
  #  j is end of substring
  return 0 if s.length == 0
  sa = s.split('')
  max = 1
  sa.each_with_index do |substring, i|
    j = i+1
    while j < sa.length && !substring.include?(sa[j])
      substring += sa[j]
      j += 1
    end
    max = [max, j-i].max
  end
  max
end

def length_of_longest_substring(s)
  stack = []
  max = 0
  s.each_char do |char|
    unless i = stack.index(char) # if char not in the stack 
      stack.push(char) # add it
    else
      stack.push(char) # add it still
      (i + 1).times {stack.shift} # remove first i + 1 elements
    end
    max = stack.length if stack.length > max
  end
  max
end

puts length_of_longest_substring("pwwkew")

wke