# Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)

point1 = (2,2)
point2 = (6,10)

slope = (point2[1] - point1[1])/(point2[0] - point1[0])
euclideanDistance = ((point2[1] - point1[1])**2 + (point2[0] - point1[0])**2)**(1/2)

print(f"Slope = {slope}")
print(f"Euclidean distance = {euclideanDistance}")