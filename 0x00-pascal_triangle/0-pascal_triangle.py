#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generate Pascal's triangle of height n
    """
    if n <= 0:
        return []
    
    triangle = []  # This will contain the entire triangle
    
    for i in range(n):
        row = [None for _ in range(i + 1)]  # Initialize the row with None values
        row[0], row[-1] = 1, 1  # First and last elements of each row are 1
        
        # For each element in between, calculate the sum of the two elements above it
        for j in range(1, len(row) - 1):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        
        triangle.append(row)  # Add the row to the triangle
    
    return triangle

# Testing the function with the provided main block

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
