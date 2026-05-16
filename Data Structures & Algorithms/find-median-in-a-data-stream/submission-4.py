import heapq

class MedianFinder:

    def __init__(self):
        self.left_h =[]
        self.right_h =[]
        self.median = None
        self.median_left=None
        self.median_right=None
        self.length = 0

    def addNum(self, num: int) -> None:
        if self.length == 0:
            self.median = num
        elif self.length % 2 == 1:
            if num >= self.median:
                heapq.heappush(self.right_h, num)
                heapq.heappush_max(self.left_h, self.median)
            else:
                heapq.heappush_max(self.left_h, num)
                heapq.heappush(self.right_h, self.median)
            self.median_left = self.left_h[0]
            self.median_right = self.right_h[0]
            self.median = None
        else:
            if num >= self.median_right:
                heapq.heappush(self.right_h, num)
                self.median=heapq.heappop(self.right_h)
            elif num>=self.median_left:
                self.median=num
            else:
                heapq.heappush_max(self.left_h, num)
                self.median=heapq.heappop_max(self.left_h)
            self.median_left=None
            self.median_right=None
        self.length +=1
        # print("num=%s, length=%s, median=%s, median_l=%s, median_r=%s, left=%s, right=%s" % (num, self.length, self.median, self.median_left, self.median_right, self.left_h, self.right_h ))
            

    def findMedian(self) -> float:
        if self.median is not None:
            return self.median
        else:
            return (self.median_left + self.median_right)/2
        
        