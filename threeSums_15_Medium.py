class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        num_len=len(nums)
        res=[]

        for i in range(0,num_len-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left=i+1
            right=num_len-1
            while left<right:
                    trip_sum=nums[i]+nums[left]+nums[right]
                    if trip_sum == 0:
                        res.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif trip_sum < 0:
                        left=left+1
                    else:
                        right=right-1

        # res=set(tuple(sorted(i)) for i in res)
        return res 
