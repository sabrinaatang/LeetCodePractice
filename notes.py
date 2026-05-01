import heapq

# 1. Initialize a list
data = [10, 5, 18, 7, 3, 12, 1]

# 2. Transform the list into a min-heap in-place
heapq.heapify(data)
print("Min-Heap after heapify:", data)
# Output: [1, 3, 10, 7, 5, 12, 18]

# 3. Add a new element
heapq.heappush(data, 4)
print("After pushing 4:", data)

# 4. Pop the smallest element
smallest = heapq.heappop(data)
print(f"Popped smallest element: {smallest}")
print("Heap after pop:", data)