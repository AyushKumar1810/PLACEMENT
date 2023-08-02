# Given a list of points on the 2-D plane and an integer K. The task is to find K closest points to the origin and print them.

# Note: The distance between two points on a plane is the Euclidean distance.

# Example:
# Input : point = [[3, 3], [5, -1], [-2, 4]], K = 2 . 

#NOTE= as we have to find the closest K points To the origin .. 
# so for finding Closest distnace to origin we will find it's distance from origin to that point by distance formula dist= (x^2+y^2) and we will campare with each other as we have to find closest to origin that means minimum distnace so we will use max heap . we will stote it into hashmap as  (dist , Coordinates {x,y}) . 
#We wil then put into heap as  (dist , Coordinates {x,y}) and use max Heap property and when sixe of max heap > k we will pop and lasty return our max Heap but only points we have to return so we will only return Points .


import heapq

def kClosest(points, k):
    heap = []  # Initialize an empty heap
    for point in points:
        dist = point[0] * point[0] + point[1] * point[1]  # Calculate the squared Euclidean distance
        heapq.heappush(heap, (-dist, point))  # Push the negative distance and the point into the heap
        if len(heap) > k:
            heapq.heappop(heap)  # If the heap size exceeds k, remove the point with the maximum negative distance
    
    return [point for dist, point in heap]  # Extract the points from the heap and return as the output

# Example usage:
points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]
k = 3
output = kClosest(points, k)

print("Input:", points)
print("Output:", output)

    

