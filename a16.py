import csv
from math import sqrt

# Function to calculate Euclidean distance
def distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# Read CSV file
filename = input("Enter CSV filename: ")
points = []

try:
    with open(filename, newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row if exists
        for row in reader:
            points.append(tuple(map(float, row)))

    # Find closest points
    closest_pair = min(
        ((p1, p2) for i, p1 in enumerate(points) for p2 in points[i+1:]),
        key=lambda pair: distance(pair[0], pair[1])
    )
    
    print("Closest Points:", closest_pair[0], "and", closest_pair[1])
    print("Minimum Distance:", distance(closest_pair[0], closest_pair[1]))

except FileNotFoundError:
    print("File not found!")
