class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_count = 0  # liczba najczęściej występującej litery w oknie
        left = 0
        max_len = 0

        for right in range(len(s)):
            count[s[right]] += 1
            max_count = max(max_count, count[s[right]])

            # Jeśli trzeba by zmienić więcej niż k liter → zmniejsz okno
            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len