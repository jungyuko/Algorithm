class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = []
        for i in range(len(nums)-1):                # 처음부터 마지막 바로 전까지 반북
            for j in range(i+1, len(nums)):         # 현재+1부터 마지막까지 반복
                if nums[i] + nums[j] == target:     # 두 수의 합이 target이라면
                    ans.append(i)                   # i, j 인덱스를 ans 배열에 추가
                    ans.append(j)
                    return ans                      # 정답 return

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}    # 각 list의 값을 key, 각 list의 index를 value
        
        for i, num in enumerate(nums):  # 입력 list만큼 반복한다.
            n = target-num              # n은 주어진 target과 해당 num의 차이 값

            if n not in dic:            # n이 딕셔너리 key에 없다면,
                dic[num] = i            # key를 num, value를 index로 딕셔너리에 저장
            else:                       # n이 딕셔너리 key에 있다면,
                return [dic[n], i]      # n의 key를 갖는 value와 현재 index 값을 return