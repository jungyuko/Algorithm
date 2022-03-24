######################################
### https://jungyuko.tistory.com/9 ###
######################################
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        letters= []    # 문자가 나오는 문장을 저장하기 위한 리스트
        digits = []    # 숫자가 나오는 문장을 저장하기 위한 리스트
        
        for log in logs:              # 입력 str 중 1개의 str씩 살펴보면서
            split = log.split(' ')    # 띄어쓰기 기준으로 split한다.
            
            if split[1].isdigit():    # 첫 번째는 식별자이므로 두 번째 문자가 숫자면
                digits.append(log)    # digits 리스트에 log를 추가한다.
            else:                     # 두 번째 문자가 문자라면
                letters.append(log)   # letters 리스트에 log를 추가한다.
        
        # letters를 정렬한다.
        # lambda x를 기준으로 정렬
        print(letters)
        letters.sort(key=lambda x: (x.split(' ')[1:],x.split(' ')[0]))
        
        print(letters)
        ans = letters + digits    # letters와 digits를 추가
        return ans