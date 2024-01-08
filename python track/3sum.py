class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)
        result = []

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums)-1
            #print("i:",i, "l:",l, "r:",r)
            
            while l < r:
                tot = nums[i] + nums[r] + nums[l]
                if tot == 0:
                    #print(r, i)
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    r -= 1
                    l += 1
                    
                elif tot < 0:
                    #print("tot<0:", nums[i], nums[l], nums[r])
                    l += 1
                    
                else:
                    r -= 1
                    #print("tot>0:",nums[i], nums[l], nums[r])
                
                #print(nums[i], nums[l], nums[r])
        return result