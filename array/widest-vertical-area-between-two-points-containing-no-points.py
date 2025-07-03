class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        h_points =[t[0] for t in points]
        h_points.sort(reverse=True)
        max_= 0
        for i in range(1,len(points)):
            j = i - 1
            max_ = max(h_points[j] - h_points[i],max_)
        return max_
            