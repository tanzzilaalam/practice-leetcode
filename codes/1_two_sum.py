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
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        results = []
        for idx in range(len(nums)):
            for idx2 in range(len(nums)):
                if idx >=idx2:
                    continue
                if nums[idx] + nums[idx2] == target:
                    results.extend([idx, idx2])
        return results
    
       
    @performance_decorator  
    def twoSum_order_n(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        
        # making dictionary
        for index, value in enumerate(nums):
            target_extra = target - value
            if target_extra in dictionary:
                result = [dictionary[target - value], index]
                return result
            dictionary[value] = index
                
        return []
    
    
if __name__ == "__main__":
    solution = Solution()
    
    # print(solution.twoSum_follwoup(nums = [2,7,11,15], target = 9))
    
    print(solution.twoSum_order_n(nums = [2,7,11,15], target = 9) == [0,1])
    print(solution.twoSum_order_n(nums = [3,2,4], target = 6) == [1,2])
    print(solution.twoSum_order_n(nums = [3,3], target = 6) == [0,1])
