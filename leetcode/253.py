class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0 
        intervals = sorted(intervals, key=lambda x:x[0])
        rooms = [0]
        for interval in intervals:
            add = False 
            for index, room in enumerate(rooms):
                if interval[0] >= room:
                    rooms[index] = interval[1]
                    add = True 
                    break 
            if not add:
                rooms.append(interval[1])
                
        return len(rooms)
        

