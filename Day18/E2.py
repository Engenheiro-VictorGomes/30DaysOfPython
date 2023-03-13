# 2. The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin,
#       4 and 8 in the positive direction. Extract these numbers from this whole text and find the distance between the two furthest particles.
#       points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']
#       sorted_points =  [-4, -3, -1, -1, 0, 2, 4, 8]
#       distance = 8 -(-4) # 12
import re
text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction."

points = re.findall(r'-?\d', text) 
print(f"points: {points}") #points = ['-1', '2', '-4', '-3', '-1', '0', '4', '8']

points = re.findall(r'-?\d+', text) 
print(f"points: {points}") #points = ['-12', '-4', '-3', '-1', '0', '4', '8']

sorted_points = sorted(map(lambda x:int(x),points))
print(f"sorted_points: {sorted_points}")

distance = sorted_points[-1:][0]-sorted_points[:1][0]
print(f"distance: {distance}")
