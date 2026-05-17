class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = list(sorted(intervals, key=lambda x: x[0]))
        results = []
        prev = intervals[0]
        for i in range(1,len(intervals)):
            current = intervals[i]
            if current[0]<=prev[1]:
                prev[1]=max(current[1], prev[1])
            else:
                results.append(prev)
                prev = current
        results.append(prev)
        return results
