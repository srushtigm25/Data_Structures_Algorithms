class Solution:
    def countSeniors(self, details: List[str]) -> int:
        np = 0
        for i in range(len(details)):
            if int(details[i][11:13]) > 60:
                np+=1
        return np

      
