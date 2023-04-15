

# 973. K Closest Points to Origin
#
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#
#
#
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].
#
#
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.


import math
class Solution:
    def kClosest(self, points, k: int):
        output = []  # dict will not work as if input contains same x,y values repeated.
        for i, j in points:
            x = math.sqrt(i ** 2 + j ** 2)
            output.append([(i, j),  x])
        sorted_list = sorted(output, key= lambda x :x[1])
        output = []
        for i in range(k):
            output.append(sorted_list[i][0])
        return output