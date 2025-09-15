class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        broken = set()
        for chr in brokenLetters:
            broken.add(chr)

        res = 0
        can = True

        for chr in text:
            if chr != " ":
                if chr in broken:
                    can = False
            elif chr == " ":
                if can == True:
                    res+=1
                can = True

        # last string
        if can == True:
            res+=1
        
        return res
