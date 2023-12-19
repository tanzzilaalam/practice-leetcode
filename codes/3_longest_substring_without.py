from typing import *
import time


def performance_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()

        # Call the original function
        result = func(*args, **kwargs)

        end_time = time.time()
        execution_time = end_time - start_time

        print(f"Function {func.__name__} took {execution_time*1000:.6f} miliseconds to execute.")

        return result

    return wrapper
    

class Solution:
    @performance_decorator  
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        length = 1
        for idx in range(len(s)):
            if idx == 0:
                continue
            old = s[start:idx]
            current = s[idx]
            if current in old:
                start = old.index(current) + 1
                length = len(s[start:idx])
            else:
                length = len(old)
                
        print(length)
        return length
            

    
    
if __name__ == "__main__":
    solution = Solution()
    
    print(solution.lengthOfLongestSubstring(s = "abcabcbb") == 3)
    print(solution.lengthOfLongestSubstring(s = "bbbbb") == 1)
    print(solution.lengthOfLongestSubstring(s = "pwwkew") == 3)
