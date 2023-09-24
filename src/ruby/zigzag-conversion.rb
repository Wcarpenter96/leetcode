# @param {String} s
# @param {Integer} num_rows
# @return {String}

require 'pry'

def convert(s, num_rows)
  if num_rows == 1 || s.length == 1
    return s
  end
  up = false
  r = 0
  rows = Hash.new {|hash, key| hash[key] = []}
  0.upto(s.length-1) do |si|
    rows[r].push(si)
    if r == 0 || r == num_rows-1
      up = !up
    end
    up ? r+=1 : r-=1
  end
  new_s = ''
  binding.pry
  0.upto(num_rows-1) do |ri|
    rows[ri].each do |si|
      new_s += s[si]
    end
  end
  new_s
end

convert("AB", 1)