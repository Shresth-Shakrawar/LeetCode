            #print(f"{x1=} {y1=} {x2=} {y2=}")
            x_diff = abs(x2-x1)
            y_diff = abs(y2-y1)
            #print(f"{x_diff=} {y_diff=}")
            steps += minDiff
            minDiff = min(x_diff,y_diff)
            x_diff -= minDiff
            y_diff -= minDiff
            if x_diff > 0:
                steps+=x_diff
            elif y_diff > 0:
                steps+= y_diff
        return steps
            
            x1,y1 = points[i][0],points[i][1]
            x2,y2 = points[i+1][0],points[i+1][1]
            return steps
        for i in range(0,len(points)-1):
        if len(points) == 1:
        steps = 0
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
class Solution: