class Solution(object):
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0

        # Znalezienie wartości minimalnej i maksymalnej
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0  # Jeśli wszystkie liczby są takie same, różnica wynosi 0

        # Obliczanie rozmiaru kubełków
        n = len(nums)
        bucket_size = max(1, (max_val - min_val) // (n - 1))  # Minimalny rozmiar kubełka to 1
        bucket_count = (max_val - min_val) // bucket_size + 1  # Ilość kubełków

        # Inicjalizacja kubełków (każdy przechowuje min i max)
        buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

        # Rozmieszczanie wartości w kubełkach
        for num in nums:
            idx = (num - min_val) // bucket_size
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)

        # Obliczanie największej różnicy między sąsiednimi kubełkami
        max_gap = 0
        prev_max = min_val  # Początkowy max to min_val, by rozpocząć iterację

        for i in range(bucket_count):
            if buckets[i][0] == float('inf'):  # Pusty kubełek
                continue

            max_gap = max(max_gap, buckets[i][0] - prev_max)  # Różnica między min w obecnym kubełku a max z poprzedniego
            prev_max = buckets[i][1]  # Aktualizacja prev_max na max obecnego kubełka

        return max_gap

# Przykład użycia
nums = [3, 6, 9, 1]
sol = Solution()
print(sol.maximumGap(nums))  # Output: 3
