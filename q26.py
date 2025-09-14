# Original tuple
T1 = (10, 20, 30, 40, 50)
print(f"Original tuple: {T1}")

# Convert the tuple to a list
list_from_tuple = list(T1)

# Modify the list (e.g., change the first element and add a new element)
list_from_tuple[0] = 100  # Change the first element
list_from_tuple.append(60) # Add a new element

# Convert the modified list back to a tuple
T1_modified = tuple(list_from_tuple)

print(f"Modified tuple: {T1_modified}")