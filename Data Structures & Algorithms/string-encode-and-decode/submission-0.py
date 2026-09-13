class Solution:

    def encode(self, strs: List[str]) -> str:
        # if not strs:
        #     return ""
        # sizes, res = [], ""

        # for s in strs:
        #     sizes.append(len(s))
        
        # for sz in sizes:
        #     res += str(sz)
        #     res += ","
        # res += '#'

        # for s in strs:
        #     res += s
        # return res
        res = ""
        for s in strs:
            res+=str(len(s))
            res+="#"
            res+=s
        return res
       

    def decode(self, s: str) -> List[str]:
        #5#hello5#world
        i = 0 
        res= []
        while i < len(s):
            j = i

            while s[j]!= '#':
                j+=1
            length = int(s[i:j])
            word = s[j+1:j+1+length]
            res.append(word)

            i = j+1+length

        return res





        # if not s:
        #     return []
        
        # sizes , res = [], []
        # i = 0 

        # while (s[i] != "#"):
        #     cur = ""
        #     while s[i] != ",":
        #         cur += s[i]
        #         i+=1
        #     sizes.append(int(cur))
        #     i+=1
        # i+=1

        # for sz in sizes:
        #     res.append(s[i:i + sz])
        #     i += sz
        # return res
            


        

