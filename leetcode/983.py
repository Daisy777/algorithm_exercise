'''
Author: ZHAO Zinan
Created: 12. March 2019

983. Minimum Cost For Tickets
''' 
class Solution:
    def mincostTickets(self, days, costs) -> int:
        if (not days) or (not costs):
            return 0

        dayBoolArr = [0]*366
        for day in days:
            dayBoolArr[day] = 1

        for index, cost in enumerate(dayBoolArr):
            if index == 0:
                continue

            if not cost:
                dayBoolArr[index] = dayBoolArr[index-1]
            else:
                dayBoolArr[index] = min(costs[0]+dayBoolArr[index-1], costs[1]+dayBoolArr[max(0, index-7)], costs[2]+dayBoolArr[max(0, index-30)])

            if index > days[len(days)-1]:
                return dayBoolArr[index]
        return dayBoolArr[365]

# test
if __name__ == '__main__':
    # print(Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2, 7, 15])) # 17
    # print(Solution().mincostTickets([1,4,6,7,8,20], [2, 7, 15])) # 11
    # print(Solution().mincostTickets([1,4,6,7,8,365], [2,7,15])) # 11
    print(Solution().mincostTickets([1,4,6,7,8,20], [7,2,15])) # 6
    # 423
    print(Solution().mincostTickets([1,2,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,20,21,24,25,27,28,29,30,31,34,37,38,39,41,43,44,45,47,48,49,54,57,60,62,63,66,69,70,72,74,76,78,80,81,82,83,84,85,88,89,91,93,94,97,99], [9,38,134]))
 