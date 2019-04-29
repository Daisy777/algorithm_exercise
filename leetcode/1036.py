import collections

class Solution:
    def isEscapePossible(self, blocked, source,  target):
        if not blocked:
            return True 
        blocked = set(map(tuple, blocked))

        def child(node, size, blocked, visited):
            x, y = node[0], node[1]
            children = []
            if x >0 and (x-1, y) not in blocked and (x-1, y) not in visited:
                children.append([x-1, y])
                visited.add((x-1, y))
            if x<size-1 and (x+1, y) not in blocked and (x-1, y) not in visited:
                children.append([x+1, y])
                visited.add((x+1, y))
            if y > 0 and (x, y-1) not in blocked and (x-1, y) not in visited:
                children.append([x, y-1])
                visited.add((x, y-1))
            if y<size-1 and (x, y+1) not in blocked and (x-1, y) not in visited:
                children.append([x, y+1])
                visited.add((x, y+1))
            return children 

        # set steps limit with bfs
        def search(blocked, source, target):
            steplimit, numsteps = len(blocked), 0
            visited = set([(source[0], source[1])])
            queue = [source]

            while(queue and numsteps <= steplimit):
                for _ in range(len(queue)):
                    node = queue.pop(0)
                    if node[0] == target[0] and node[1] == target[1]:
                        return True
                    
                    queue.extend(child(node, 1000000, blocked, visited))
                # print(queue)
                numsteps += 1
            if len(queue) > 0:
                return True
            
            return False
        return search(blocked, source ,target) and search(blocked, target, source)

if __name__ == '__main__':
    block = [[100059,100063],[100060,100064],[100061,100065],[100062,100066],[100063,100067],[100064,100068],[100065,100069],[100066,100070],[100067,100071],[100068,100072],[100069,100073],[100070,100074],[100071,100075],[100072,100076],[100073,100077],[100074,100078],[100075,100079],[100076,100080],[100077,100081],[100078,100082],[100079,100083],[100080,100082],[100081,100081],[100082,100080],[100083,100079],[100084,100078],[100085,100077],[100086,100076],[100087,100075],[100088,100074],[100089,100073],[100090,100072],[100091,100071],[100092,100070],[100093,100069],[100094,100068],[100095,100067],[100096,100066],[100097,100065],[100098,100064],[100099,100063],[100098,100062],[100097,100061],[100096,100060],[100095,100059],[100094,100058],[100093,100057],[100092,100056],[100091,100055],[100090,100054],[100089,100053],[100088,100052],[100087,100051],[100086,100050],[100085,100049],[100084,100048],[100083,100047],[100082,100046],[100081,100045],[100080,100044],[100079,100043],[100078,100044],[100077,100045],[100076,100046],[100075,100047],[100074,100048],[100073,100049],[100072,100050],[100071,100051],[100070,100052],[100069,100053],[100068,100054],[100067,100055],[100066,100056],[100065,100057],[100064,100058],[100063,100059],[100062,100060],[100061,100061],[100060,100062]]
    # print(Solution().isEscapePossible([[0, 1], [1, 0]], [1, 1], [0, 0]))
    print(Solution().isEscapePossible(block, [100079,100063], [999948,999967]))