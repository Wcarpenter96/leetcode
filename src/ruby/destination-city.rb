# @param {String[][]} paths
# @return {String}
def dest_city(paths)
  origins = paths.map { |path| path[0] }
  paths.map { |path| path[1] }.each do |city| 
    unless origins.include? city
      return city
    end
  end
end

def dest_city(paths)
  city = []
  paths.each do |dest|
    city<<dest[1]
  end
  paths.each do |origin|
    city.delete(origin[0])
  end
  return city[0]
end