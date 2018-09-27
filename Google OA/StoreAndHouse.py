"""
Given two arrays of integers representing the location of stores&houses, output the nearest store for all the houses.
If two stores share the nearest distance, choose the left one.

For example:
stores = [3,5]
houses = [6,2,4]

stores = [1,4,6,8,10]
houses = [2,5,8,9,12]
"""

class Solution(object):
    def nearestStore(self, stores, houses):
        stores_num = len(stores)
        houses_num = len(houses)
        if stores_num == 1:
            return [stores[0]]*houses_num
        ans = [0]*houses_num
        cnt = 0
        for house in houses:
            start, end = 0, len(stores)-1
            equal = False
            while start+1 != end:
                mid_index = (start+end)/2
                store = stores[mid_index]
                if house == store:
                    ans[cnt] = store
                    cnt += 1
                    equal = True
                    break
                if house > store:
                    start = mid_index
                else:
                    end = mid_index
            if not equal:
                left_store, right_store = stores[start], stores[end]
                ans[cnt] = left_store if  house-left_store <= right_store-house else right_store
                cnt += 1
        return ans

stores = [2,4,5,8,10]
houses = [1,3,5,9,12]
S = Solution()
print S.nearestStore(stores, houses)




