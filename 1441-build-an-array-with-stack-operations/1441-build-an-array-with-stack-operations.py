class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        stream_num = 1
        
        for num in target:
            while stream_num < num:
                res.append("Push")
                res.append("Pop")
                stream_num += 1
                
            res.append("Push")
            stream_num += 1
            
        return res