#n^2

def cross(ax: int, ay: int, bx: int, by: int) -> int:
    # (ax, ay) x (bx, by) -> wartość z (skalarnie w 2D)
    return ax * by - ay * bx

def area2(a: Tuple[int,int], b: Tuple[int,int], c: Tuple[int,int]) -> int:
    # Zwraca 2 * pole trójkąta ABC (całkowite, bez dzielenia)
    return abs(cross(b[0]-a[0], b[1]-a[1], c[0]-a[0], c[1]-a[1]))

def convex_hull(points: List[Tuple[int,int]]) -> List[Tuple[int,int]]:
    # Monotone chain: O(n log n). Zwraca wierzchołki w porządku CCW, bez powtórki pierwszego.
    P = sorted(set(points))  # usuwamy duplikaty; sortujemy po (x,y)
    if len(P) <= 1:
        return P

    lower = []
    for p in P:
        while len(lower) >= 2 and cross(lower[-1][0]-lower[-2][0], lower[-1][1]-lower[-2][1],
                                        p[0]-lower[-1][0], p[1]-lower[-1][1]) <= 0:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(P):
        while len(upper) >= 2 and cross(upper[-1][0]-upper[-2][0], upper[-1][1]-upper[-2][1],
                                        p[0]-upper[-1][0], p[1]-upper[-1][1]) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]  # bez domykania

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        P = [tuple(p) for p in points]
        if len(P) < 3:
            return 0.0

        hull = convex_hull(P)
        m = len(hull)
        if m < 3:
            return 0.0

        # Rotating calipers na wielokącie wypukłym: O(m^2)
        best2 = 0
        for i in range(m):
            j = (i + 1) % m
            k = (j + 1) % m
            # przesuwamy j wokół raz dla danego i
            while j != i:
                # dla pary (i, j) dociągaj k tak długo, jak pole rośnie
                while True:
                    nxt = (k + 1) % m
                    if nxt == i:
                        break
                    if area2(hull[i], hull[j], hull[nxt]) >= area2(hull[i], hull[j], hull[k]):
                        k = nxt
                    else:
                        break
                best2 = max(best2, area2(hull[i], hull[j], hull[k]))
                j = (j + 1) % m
                if j == k:
                    k = (k + 1) % m
                    if k == i:
                        break

        return best2 / 2.0

#n^3
        '''
from typing import List, Tuple

def cross(ax: int, ay: int, bx: int, by: int) -> int:
    return ax * by - ay * bx

def area2(a: Tuple[int,int], b: Tuple[int,int], c: Tuple[int,int]) -> int:
    # 2 * pole trójkąta ABC (na intach, bez dzielenia)
    return abs(cross(b[0]-a[0], b[1]-a[1], c[0]-a[0], c[1]-a[1]))

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        P = [tuple(p) for p in points]
        n = len(P)
        if n < 3:
            return 0.0

        best2 = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a2 = area2(P[i], P[j], P[k])
                    if a2 > best2:
                        best2 = a2
        return best2 / 2.0
'''


