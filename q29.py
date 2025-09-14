# Define the tuples
t1 = (10, 20, 30, 40, 50)
t2 = (60, 70, 80, 60)

# Define the items to check for
xt1 = 10
xt2 = 60

# Check if xt1 is in t1
if xt1 in t1:
    print(f"The item {xt1} is present in tuple t1.")
else:
    print(f"The item {xt1} is not present in tuple t1.")

# Check if xt2 is in t2
if xt2 in t2:
    print(f"The item {xt2} is present in tuple t2.")
else:
    print(f"The item {xt2} is not present in tuple t2.")

# You can also check for other values in a similar way
# For example, checking for a value not present in t1
not_in_t1 = 100
if not_in_t1 in t1:
    print(f"The item {not_in_t1} is present in tuple t1.")
else:
    print(f"The item {not_in_t1} is not present in tuple t1.")



    T1 = (10, 20, 30, 40, 50)
T2 = (60, 70, 80, 60) # T2 is defined but not used in the core logic as per the request
X = 60 # The item to check for in T1

# Check if X is NOT in T1
if X not in T1:
    print(f"The item {X} is NOT found in T1.")
else:
    print(f"The item {X} IS found in T1.")




    # Define the first tuple
T1 = (10, 20, 30, 40, 50)

# Define the second tuple
T2 = (60, 70, 80, 60)

# Concatenate T1 and T2 to create a new tuple
T_new = T1 + T2

# Print the new concatenated tuple
print(f"The new concatenated tuple is: {T_new}")





T1 = (10, 20, 30, 40, 50)
T2 = (60, 70, 80, 60)

# Repeat T1 five times
repeated_T1 = T1 * 5

# Print the original and repeated tuples
print(f"Original T1: {T1}")
print(f"Repeated T1 (5 times): {repeated_T1}")
print(f"\nOriginal T2: {T2}")





def get_item_at_index(input_list, index):
    """
    Retrieves the item from a list at the specified index.

    Args:
        input_list (list): The list from which to retrieve the item.
        index (int): The index of the item to retrieve.

    Returns:
        Any: The item at the specified index, or None if the index is out of bounds.
    """
    if -len(input_list) <= index < len(input_list):
        return input_list[index]
    else:
        print(f"Error: Index {index} is out of bounds for the list.")
        return None
    





# Example usage:
my_list = ["apple", "banana", "cherry", "date", "elderberry"]

# Get item at a positive index
item_positive_index = get_item_at_index(my_list, 2)
print(f"Item at index 2: {item_positive_index}")

# Get item at a negative index (counts from the end)
item_negative_index = get_item_at_index(my_list, -1)
print(f"Item at index -1: {item_negative_index}")

# Attempt to get item at an out-of-bounds index
item_out_of_bounds = get_item_at_index(my_list, 10)
print(f"Item at index 10: {item_out_of_bounds}")

item_out_of_bounds_negative = get_item_at_index(my_list, -6)
print(f"Item at index -6: {item_out_of_bounds_negative}")






def count_specific_items(t1, t2, target_values):
  """
  Counts the total number of items in two tables (lists/tuples) that match 
  any of the specified target values.

  Args:
    t1: The first table (list or tuple).
    t2: The second table (list or tuple).
    target_values: A list or tuple of values to count.

  Returns:
    The total count of matching items across both tables.
  """
  count = 0
  for item in t1:
    if item in target_values:
      count += 1
  for item in t2:
    if item in target_values:
      count += 1
  return count

# Define the tables
T1 = (10, 20, 30, 40, 50)
T2 = (60, 70, 80, 60)

# Define the target values to count (all values present in T1 and T2)
# If you only want to count specific target values, you would define them here.…






# Define the tuples
t1 = (10, 20, 30, 40, 50)
t2 = (60, 70, 80, 60)

# Find the minimum value in t1
min_t1 = min(t1)

# Find the minimum value in t2
min_t2 = min(t2)

# Print the minimum values
print(f"The minimum value in tuple t1 is: {min_t1}")
print(f"The minimum value in tuple t2 is: {min_t2}")






def find_max_in_tuples(T1, T2):
  """
  Finds the maximum value across two tuples.

  Args:
    T1: The first tuple.
    T2: The second tuple.

  Returns:
    The item with the maximum value found in either T1 or T2.
  """
  max_t1 = max(T1)  # Find the maximum in T1
  max_t2 = max(T2)  # Find the maximum in T2
  return max(max_t1, max_t2) # Return the overall maximum

# Define the tuples
T1 = (10, 20, 30, 40, 50)
T2 = (60, 70, 80, 60)

# Call the function and print the result
overall_max = find_max_in_tuples(T1, T2)
print(f"The item with the maximum value from T1 and T2 is: {overall_max}")