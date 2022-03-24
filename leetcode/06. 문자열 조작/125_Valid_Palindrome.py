######################################
### https://jungyuko.tistory.com/7 ###
######################################
class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
      
        for char in s:                      # 모든 입력 s를 반복
            if char.isalnum():              # 각 단어가 문자 혹은 숫자인 경우,
                strs.append(char.lower())   # 소문자로 변경하여 strs 배열에 저장
        
        while len(strs) > 1:                # strs의 길이가 1보다 크다면,
            if strs.pop(0) != strs.pop():   # strs의 1번째 값과 마지막 값이 같지 않다면,
                return False                # False 출력
        
        return True                         # 모든 경우를 통과하면 True
    
            