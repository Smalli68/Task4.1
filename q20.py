# Define a sample tuple
my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

print(f"Original tuple: {my_tuple}")

# 1. Basic slicing: elements from index 2 (inclusive) to 6 (exclusive)
slice1 = my_tuple[2:6]
print(f"Slice from index 2 to 5: {slice1}")

# 2. Slicing from the beginning to a specific index (exclusive)
slice2 = my_tuple[:4]
print(f"Slice from beginning to index 3: {slice2}")

# 3. Slicing from a specific index (inclusive) to the end
slice3 = my_tuple[5:]
print(f"Slice from index 5 to end: {slice3}")

# 4. Slicing with a step: every second element from index 1 to 8
slice4 = my_tuple[1:9:2]
print(f"Slice with step 2 from index 1 to 8: {slice4}")

# 5. Slicing with negative indices: last four elements
slice5 = my_tuple[-4:]
print(f"Last four elements using negative indexing: {slice5}")

# 6. Slicing the entire tuple (creates a shallow copy)
slice6 = my_tuple[:]
print(f"Entire tuple (shallow copy): {slice6}")