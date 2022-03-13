require 'pry'
# @param {Integer[]} prices
# @return {Integer}

def max_profit(prices)
  min = prices[0]
  max = 0
  profit = 0
  prices.each do |price|
    if price < min
      min = price
    else
      profit = price-min
      if profit > max
        max = profit
      end
    end
    binding.pry
  end
  max
end

# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
  min = prices[0]
  max = 0
  profit = 0
  prices.each do |price| 
    min = [price,min].min
    max = [price-min, max].max
  end
  max
end


max_profit([7,1,5,3,6,4])

