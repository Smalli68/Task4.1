# Initial tuple containing a list
my_tuple = (11, [22, 33], 44, 55)

print(f"Original tuple: {my_tuple}")

# Access the list within the tuple and modify its first element
# The list is at index 1 of the tuple, and the element 22 is at index 0 of that list.
my_tuple[1][0] = 222

print(f"Modified tuple: {my_tuple}")