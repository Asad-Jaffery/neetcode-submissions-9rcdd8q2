import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # iterate through the points and find the distance for each one to the orgigin 
        # add those all to a hashMap - which contains {point: distance}
        # return the k points that are the closest
      



        # heap will contain points based on their 
        # tuple - (distance, point) 
        # heapify (O(n)) 
        # pop K elements and return them
        distances = []
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            distances.append((distance, point))
        
        heapq.heapify(distances)
        res = []
        for i in range(k):
            res.append(heapq.heappop(distances)[1])

        return res

            

        

        


        