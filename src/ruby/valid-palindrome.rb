# @param {String} s
# @return {Boolean}
def is_palindrome(s)
    s.strip.downcase.gsub(/[^0-9a-z ]|\s/i, '') == s.strip.downcase.gsub(/[^0-9a-z ]|\s/i, '').reverse
end