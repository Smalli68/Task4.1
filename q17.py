def check_element_in_tuple(target_element, input_tuple):
  """
  Checks if a given element exists within a tuple.

  Args:
    target_element: The element to search for.
    input_tuple: The tuple to search within.

  Returns:
    True if the element is found in the tuple, False otherwise.
  """
  return target_element in input_tuple

# Example usage:
my_tuple = (10, 20, "hello", 30, "world")

# Check for an element that exists
element_to_find_1 = 20
if check_element_in_tuple(element_to_find_1, my_tuple):
  print(f"'{element_to_find_1}' exists in the tuple.")
else:
  print(f"'{element_to_find_1}' does not exist in the tuple.")

# Check for an element that does not exist
element_to_find_2 = 50
if check_element_in_tuple(element_to_find_2, my_tuple):
  print(f"'{element_to_find_2}' exists in the tuple.")
else:
  print(f"'{element_to_find_2}' does not exist in the tuple.")

# Check for a string element
element_to_find_3 = "hello"
if check_element_in_tuple(element_to_find_3, my_tuple):
  print(f"'{element_to_find_3}' exists in the tuple.")
else:
  print(f"'{element_to_find_3}' does not exist in the tuple.")