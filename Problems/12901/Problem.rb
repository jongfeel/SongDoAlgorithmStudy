def solution(a, b)
    return Time.new(2016,a,b).strftime("%a").upcase
end

puts solution(5, 24)