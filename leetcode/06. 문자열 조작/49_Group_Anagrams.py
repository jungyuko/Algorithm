#######################################
### https://jungyuko.tistory.com/11 ###
#######################################
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # 존재하지 않는 key가 입력될 경우, KeyError가 발생
        # 에러가 나지 않도록 항상 디폴트를 생성해주는 defaultdict() 선언
        anagrams = collections.defaultdict(list)  
   
        # 입력 strs의 각 단어마다 반복
        for word in strs:          
            # 각 단어를 정렬 후, 문자열로 변환
            # 애너그램끼리는 같은 key를 가지게 됨
            # 이에 따라 append()를 추가하는 형태로 저장
            anagrams[''.join(sorted(word))].append(word)    
        

        return list(anagrams.values())