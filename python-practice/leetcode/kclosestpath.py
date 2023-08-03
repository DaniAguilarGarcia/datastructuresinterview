#sort array with a custom comparator function
#return the first k elements of the array

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[list[int]]:
        #sort the list with custom comparator function
        points.sort(key=self.squared_distance)

        return points[:k]

    def squared_distance(self, point: List[int]) -> int:
        #calculate and return squared Euclidean distance
        return point[0] ** 2 + point[1] ** 2

#complexity o(nlogn)