#my solution
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #convert to dictionary
        nums_dict = dict(enumerate(nums))
        
        for i,j in nums_dict.items():
            for x,y in nums_dict.items():
                if j == target - y and x != i:
                    return [i, x]
        return []

#best solution O(n) time
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i

#two pointer solution for two-sum II WHERE THE ARRAY IS SORTED
# two-pointer
def twoSum1(self, numbers, target):
    l, r = 0, len(numbers)-1
    while l < r:
        s = numbers[l] + numbers[r]
        if s == target:
            return [l+1, r+1]
        elif s < target:
            l += 1
        else:
            r -= 1