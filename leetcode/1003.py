class Solution:
    def isValid(self, S: str) -> bool:
        previous = S
        while(True):
            after = ''.join(previous.split('abc'))
            if previous == after:
                return False
            if len(after) == 0:
                return True
            previous = after