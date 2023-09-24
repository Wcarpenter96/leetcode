# https://dev.to/mwong068/quick-sort-in-ruby-2302
class ArraySorter
  def initialize(array:)
    @array = array
  end

  def quick_sort(array=@array, first=0, last=array.length-1)
    if first < last
      j = partition(array, first, last)
      quick_sort(array, first, j-1)
      quick_sort(array, j+1, last)
    end
    return array
  end

  private
  
  def partition(array, first, last)
    pivot = array[last]
    pIndex = first
    i = first
      while i < last
        if array[i].to_i <= pivot.to_i
          array[i], array[pIndex] = array[pIndex], array[i]
          pIndex += 1
        end
      i += 1
      end
      array[pIndex], array[last] = array[last], array[pIndex]
      return pIndex
  end
end

array_sorter = ArraySorter.new(array: [2,1,4,3])

puts array_sorter.quick_sort