#######################################
### https://jungyuko.tistory.com/10 ###
#######################################

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        lowers = paragraph.lower()           # 입력 문자열을 소문자로 변경
        lowers = lowers.replace(",", " ")    # 특수 문자들을 대체한다.
        lowers = lowers.replace(".", " ")
        lowers = lowers.replace("!", " ")
        lowers = lowers.replace("?", " ")
        lowers = lowers.replace(";", " ")
        lowers = lowers.replace("'", " ")    
        words = lowers.split()               # 띄어쓰기 기준으로 나눠준다. 
				 
        # word는 words에 있는 단어이며, 
        # word가 banned에 있는 단어가 아니고, 아무것도 안적힌 문자가 아닌 word들을 list에 추가       
        words = [word for word in words if word not in banned and word != '']
				
        # Counter() 함수를 사용하여 words에 있는 갯수를 반환한다.        
        cnt_dic = Counter(words)

        # Counter의 key, value쌍을 list형태로 저장
        cnt_lst = list(cnt_dic.items())
        print(cnt_lst)
        # 정렬
        sorted_lst = sorted(cnt_lst, key=lambda x: -x[1])
        print(sorted_lst)    
        # 가장 앞에 있는 단어를 ans로
        ans = sorted_lst[0][0]
        
        return ans