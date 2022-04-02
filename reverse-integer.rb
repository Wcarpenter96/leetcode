def reverse(x)
  num = 0
  x.abs.digits.count.times do |i|
    num += x.abs / 10**i % 10 * 10**(x.abs.digits.count-1-i)
  end
  num *= x.negative? ? -1:1
end

puts reverse(-123)