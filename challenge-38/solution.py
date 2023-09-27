# Name: Las Sumas 
# Path: solution.py
# Author: IOxee
# TimeStamp: 27-09-2023 13:54:21

from typing import List, Optional

def find_combinations(nums: List[int], target: int) -> List[List[int]]:
    solutions = []
    
    def dfs(start: int, target: int, path: List[int]) -> None:
        if target == 0:
            solutions.append(path[:])
            return
        if target < 0:
            return
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1, target - nums[i], path)
            path.pop()
            
    nums.sort()
    dfs(0, target, [])
    
    return solutions

test_cases = [
    {'nums': [1, 5, 3, 2], 'target': 6, 'expected': [[1, 2, 3], [1, 5]]},
    {'nums': [1, 1, 1, 1], 'target': 4, 'expected': [[1, 1, 1, 1]]},
    {'nums': [1, 2, 3, 4, 5], 'target': 10, 'expected': [[1, 4, 5], [2, 3, 5]]},
    {'nums': [1, 2, 3], 'target': 7, 'expected': []},
    {'nums': [5, 5, 5], 'target': 15, 'expected': [[5, 5, 5]]},
    {'nums': [], 'target': 0, 'expected': []},
    {'nums': [1, 2, 3, 4], 'target': 0, 'expected': []}
]

results = []
for i, test_case in enumerate(test_cases):
    nums, target, expected = test_case['nums'], test_case['target'], test_case['expected']
    result = find_combinations(nums, target)
    is_passed = result == expected
    results.append({
        'test_case': i + 1,
        'passed': is_passed,
        'result': result,
        'expected': expected
    })

print('\n'.join([
    f"{'Test Case':<10}{'Passed':<10}{'Result':<40}{'Expected':<40}",
    *[
        f"{r['test_case']:<10}{r['passed']:<10}{str(r['result']):<40}{str(r['expected']):<40}"
        for r in results
    ]
]))