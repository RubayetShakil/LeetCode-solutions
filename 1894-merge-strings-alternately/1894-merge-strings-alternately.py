class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        len1, len2= len(word1), len(word2)
        
        small_reng= len2
        big_reng=len1
        c=0

        if len1<len2: small_reng, big_reng, c = len1, len2, 1


        new_word=""
        i=0
        while i<small_reng:
            new_word+=word1[i]+word2[i]
            i+=1

        if len1==len2: return new_word

        if c==1: final_word=self.remaining_words(word2, len2, i, new_word)

        else: final_word=self.remaining_words(word1, len1, i, new_word)

        return final_word
        
        



    def remaining_words(self, word, lenght, i, new_word):

        for x in range (i, lenght):
            new_word+=word[x]

        return new_word


        


        

