class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)      # 입력 배열을 정렬
        
        ans = 0                                     # 정답 ans 초기값 설정
        for i in range(0, len(sorted_nums), 2):     # 정렬된 배열을 2칸씩 점프하면서 반복
            ans += sorted_nums[i]                   # 정답 ans에 홀수 번째 값을 추가
        # ans = sum(sorted_nums[::2])       # 위의 3줄을 이와같이 한줄로 표현가능
        return ans