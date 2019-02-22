# fault : use <- in line 11 (inner loop) as we need to move forward even though
# the house is in the middle of two heaters
class Solution:
    def findRadius(self, houses: 'List[int]', heaters: 'List[int]') -> 'int':
        houses.sort()
        heaters.sort()
        ptr_house = 0
        ptr_heater = 0
        max_dist = 0
        while(ptr_house < len(houses)):
            while(ptr_heater < len(heaters)-1 and abs(houses[ptr_house]-heaters[ptr_heater+1]) <= abs(houses[ptr_house] - heaters[ptr_heater])):
                ptr_heater += 1
            max_dist = max(max_dist, abs(houses[ptr_house]-heaters[ptr_heater]))

            ptr_house += 1
        return max_dist



# test
if __name__ == '__main__':
    print(Solution().findRadius([1, 2, 3, 4], [1, 2, 3, 4]))