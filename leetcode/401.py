'''
Author:    ZHAO Zinan
Created: 01/17/2019

401. Binary Watch
'''
class Solution:
    def readBinaryWatch(self, num):
        import itertools
        """
        :type num: int
        :rtype: List[str]
        """
        # if num > 10:
        #     raise Exception()

        hourLight = [1, 2, 4, 8]
        minuteLight = [1,2,4,8,16,32]
        result = []

        for i in range(num+1):
            # i in hour, num-i in minute
            if i>4:
                break
            if num-i>6:
                continue

            hour = [sum(l) for l in list(itertools.combinations(hourLight, i))]
            minute = [sum(l) for l in list(itertools.combinations(minuteLight, num-i))]

            for h in hour:
                if h < 12:
                    for m in minute:
                        if m < 60:
                            result.append(f'{h}:{m:02}')
        return result


# test
if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
    #  ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
    #  "0:32"]
    
    print(Solution().readBinaryWatch(2))
    # ["0:03","0:05","0:06","0:09","0:10","0:12","0:17","0:18","0:20","0:24","0:33","0:34","0:36","0:40","0:48","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]