class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        operator = None 
        for char in s:
            if char.isdigit():
                num 