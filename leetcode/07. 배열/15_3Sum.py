### 브루트포스 1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []                # 정답 
        nums = sorted(nums)     # sorting!
        
        for i in range(len(nums)-2):                # 0부터 num-2까지 반복    
            for j in range(i+1, len(nums)-1):       # i+1부터 num-1까지 반복
                for k in range(j+1, len(nums)):     # j+1부터 num까지 반복
                    lst = []                        # 임시 정답 조합 리스트 저장 파라미터
                    if nums[i]+nums[j]+nums[k] == 0:    # 3 수의 합이 0이라면
                        lst.append(nums[i])             # lst에 3 값을 저장
                        lst.append(nums[j])
                        lst.append(nums[k])
                        ans.append(lst)                 # lst를 ans에 추가
        
        
        # ans의 각 n번째 lst값을 tuple로 변환함
        # set형태로 만들면 중복값이 제거
        # 제거된 형태를 다시 list로 변환
        ans = list(set([tuple(a) for a in ans]))        
        
        return ans

### 브루트포스 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []                # 정답 ans
        nums = sorted(nums)     # sorting!
        
        for i in range(len(nums)-2):                # 0부터 num-2까지 반복
            if i > 0 and nums[i] == nums[i-1]:      # 
                continue
                
            for j in range(i+1, len(nums)-1):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                for k in range(j+1, len(nums)):
                    if k > j+1 and nums[k] == nums[k-1]:
                        continue

                    if nums[i] + nums[j] + nums[k] == 0:
                        # print(nums[i], nums[j], nums[k])
                        ans.append([nums[k], nums[j], nums[i]])
                        
        return ans