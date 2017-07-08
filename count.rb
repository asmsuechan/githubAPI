require 'csv'
ary1 = []
ary2 = []

CSV.foreach('countries.csv.part1') do |row|
  ary1 << row[0]
end

CSV.foreach('countries.csv') do |row|
  ary2 << row[0]
end

ary = ary1 + ary2

p ary.inject(Hash.new(0)){|hash, a| hash[a] += 1; hash}.sort_by{ |_, v| -v }
