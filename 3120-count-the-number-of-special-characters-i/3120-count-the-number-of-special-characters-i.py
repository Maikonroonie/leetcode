class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        res = 0
        st = set()
        for ch in word:
            st.add(ch)
        for ch in word:
            if ch.lower() in st and ch.upper() in st:
                res += 1
                st.remove(ch)
        return res        