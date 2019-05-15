'''
Author:    ZHAO Zinan
Created: 14-May-2019

981. Time Based Key-Value Store
'''

# hash table of heap queue
import collections 
import heapq

class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        heapq.heappush(self.dict[key], (-timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        larger = []
        target = ""
        while(self.dict[key]):
            value = heapq.heappop(self.dict[key]) 
            larger.append(value) 

            if value[0] >= -timestamp:
                target = value[1] 
                break
        for l in larger:
            heapq.heappush(self.dict[key], l) 

        return target 

        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# test
if __name__ == '__main__':
    # test case 1
    timemap = TimeMap()
    timemap.set('foo', 'bar', 1)
    print(timemap.get('foo',1))
    print(timemap.get('foo', 3))
    timemap.set('foo', 'bar2', 4) 
    print(timemap.get('foo', 4))
    print(timemap.get('foo', 5))
    # [null,null,"bar","bar",null,"bar2","bar2"]

    # test case2 
    timemap = TimeMap()
    timemap.set("love","high",10)
    timemap.set("love","low",20)
    print(timemap.get("love",5))
    print(timemap.get("love",10))

    print(timemap.get("love",15))
    print(timemap.get("love",20))
    print(timemap.get("love",25))
    # [null,null,null,"","high","high","low","low"]


