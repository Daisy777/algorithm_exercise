class Solution:
    def oddEvenJumps(self, A) -> int:
        if not A:
            return 0
        if len(A) == 1:
            return 1

        # record the location of each A element
        A_loc = {}
        numA = len(A)
        for index, ele in enumerate(A):
            if ele not in A_loc:
                A_loc[ele] = index

        A.sort()
        print(A)
        smaller = [-1]*numA
        greater = [-1]*numA

        greater[A_loc[A[0]]] = A_loc[A[1]]
        
        for i in range(1, numA-1):
            if A_loc[A[i-1]] > A_loc[A[i]]:
                smaller[A_loc[A[i]]] = A_loc[A[i-1]] 
            if A_loc[A[i+1]] > A_loc[A[i]]:
                greater[A_loc[A[i]]] = A_loc[A[i+1]] 
        
        print(smaller)
        print(greater)
        can_reach_odd = [0]*numA
        can_reach_even = [0]*numA
        can_reach_odd[numA-1] = 1
        can_reach_even[numA-1] = 1
        for i in range(numA-2, -1, -1):
            # when in nodei, it is odd jump
            nextloc = greater[A_loc[A[i]]]
            if nextloc >= 0 and nextloc < numA:
                can_reach_odd[i] = can_reach_even[nextloc]

            # when in nodej, it is even jump
            nextloc = smaller[A_loc[A[i]]]
            if nextloc >= 0 and nextloc < numA:
                can_reach_even[i] = can_reach_odd[nextloc]

        print(can_reach_odd)
        print(can_reach_even)
        return sum(can_reach_odd)

# test
if __name__ == '__main__':
    print(Solution().oddEvenJumps([10, 13, 12, 14, 15])) # 2
    print(Solution().oddEvenJumps([2, 3, 1, 1,4])) # 3
    print(Solution().oddEvenJumps([5, 1, 3, 4, 2])) # 3
