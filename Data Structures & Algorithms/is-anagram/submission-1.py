class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # first check the 
        
        if len(s) != len(t):
            return False

        # get a dict of s , char: count

        dict_count={}

        for i in s:
            dict_count[i] = dict_count.get(i,0)+1
        
        # now check the freq of character in t to that of char count in dict.

        for i in t:
            if i not in dict_count:
                return False
            dict_count[i] -=1

            if dict_count[i] <0:
                return False
           
                
        return True
                    

        

         
        

                    
                


        