class Solution:
    def trap(self, height: List[int]) -> int:
        empty_size = []
        
        if len(height) <= 2:  # 주어진 height의 길이가 2보다 작으면
            return 0          # 채워질 물이 없으므로 0을 return
            
        left = [0 for i in range(len(height))]    # height의 길이가 같은 배열 선언
        right =[0 for i in range(len(height))]    # height의 길이가 같은 배열 선언
        
        max_num = height[0]                      # 초기 값은 height 배열의 첫 번째 인자
        for i in range(len(height)):             # height 길이만큼 반복
            max_num = max(max_num, height[i])    # max_num과 현재 height값 중 큰 값을 max_num에 할당
            left[i] = max_num                    # 선택된 max_num 값을 left배열에 추가한다.
             
        max_num = height[len(height)-1]           # 배열의 뒤부터 돌 것이니 초기 값은 height 배열의 마지막 인자
        for i in range(len(height)-1, -1, -1):    # height 길이만큼 반복 
            max_num = max(max_num, height[i])     # max_num과 현재 height값 중 큰 값을 max_num에 할당
            right[i] = max_num                    # 선택된 max_num 값을 right 배열에 추가한다.
            
        for i in range(len(height)):                            # height 길이만큼 반복
            empty_size.append(min(left[i], right[i])-height[i]) # left 배열과 right 배열의 값 중 작은 값과 
                                                                # height 값을 뺀 것이 물의 높이
        
        ans = 0                             
        for i in range(len(empty_size)):    # height의 길이만큼 반복
            ans += empty_size[i]            # 물의 높이 만큼 계속 더하면 정답값이 됨
            
        return ans