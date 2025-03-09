class Solution(object):
    def sortPeople(self, names, heights):
        n=len(names)
        for i in range(n):
            for j in range(0, n-i-1):
                if heights[j]<heights[j+1]:
                    heights[j], heights[j+1] = heights[j+1], heights[j]
                    names[j], names[j+1] = names[j+1], names[j]
        return names #bubble sort, i know it is not optimal but yeah it works tho
