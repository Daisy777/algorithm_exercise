class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        index = {}

        for person in people:
            if person[1] not in index.keys():
                index[person[1]] = [person]
            else:
                index[person[1]].append(person)

        # extract person[1] = 0
        result = []
        result.extend(sorted(index[0], key=lambda x:x[0]))

        # insert into result 
        keys = list(index.keys())
        keys.remove(0)
        keys.sort()
        for key in keys:
            persons = index[key]
            for person in persons:
                cnt = 0
                for i, item in enumerate(result):
                    if item[0] >= person[0]:
                        cnt += 1
                    if cnt == person[1]:
                        result.insert(i+1, person)

        return result

# test
if __name__ == '__main__':
    print(Solution().reconstructQueue([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]))    
    # [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]