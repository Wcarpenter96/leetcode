require 'pry'

# @param {String} digits
# @return {String[]}
def letter_combinations(digits)
  return [] if digits.length == 0
  num_map = {
    '2' => %w(a b c),
    '3' => %w(d e f),
    '4' => %w(g h i),
    '5' => %w(j k l),
    '6' => %w(m n o),
    '7' => %w(p q r s),
    '8' => %w(t u v),
    '9' => %w(w x y z)
  }
  digit_nums = []
  digits.split('').each do |digit|
    digit_nums.push(num_map[digit])
  end
  digit_nums[0].product(*digit_nums.drop(1)).map {|combo| combo.join('')}
end

digits = ''
puts letter_combinations(digits)