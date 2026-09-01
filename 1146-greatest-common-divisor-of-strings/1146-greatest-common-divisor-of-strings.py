class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        if str1+str2!=str2+str1:
            return ""

        new_str1, new_str2=len(str1), len(str2)



        while True:
            remain=new_str1%new_str2
            if remain==0: return str1[:new_str2]
            new_str1, new_str2=new_str2, remain

            




        