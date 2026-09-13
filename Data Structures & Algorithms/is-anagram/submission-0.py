class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t) and len(s)==len(t)
        if len(s) != len(t):
            return False
        
        count = defaultdict(int)

        for str in s:
            count[str] +=1
        
        for str in t:
            count[str] -=1

        for v in count.values():
            if v != 0:
                return False
        return True
       

      
