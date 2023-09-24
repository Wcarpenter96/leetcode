class Solution:
    def sum_indexes(self,l):
        index_sum = {}
        for i,l in enumerate(l):
            index_sum[l] = i
        return index_sum
    def findRestaurant(self, list1, list2):
        index_sum = {}
        index_sum1 = self.sum_indexes(list1)
        index_sum2 = self.sum_indexes(list2)
        for key in index_sum1:
            if key in index_sum2:
                index_sum[key] = index_sum1[key] + index_sum2[key]
        m = min(index_sum.values())
        return [x for x in index_sum if index_sum[x] == m ]

list1 = ["Tapioca Express","Shogun","Burger King","KFC"]
list2 = ["Shogun","Tapioca Express","Hungry Hunter Steakhouse"]
print(Solution().findRestaurant(list1, list2))

