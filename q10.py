def are_all_items_same(input_tuple):
  """
  Checks if all items in a given tuple are identical.

  Args:
    input_tuple: The tuple to be checked.

  Returns:
    True if all items in the tuple are the same, False otherwise.
    Returns True for an empty tuple.
  """
  if not input_tuple:  # Handle empty tuple case
    return True
  
  # Convert the tuple to a set. If all items are the same, the set will
  # contain only one element.
  return len(set(input_tuple)) == 1

# Test cases
tuple1 = (1, 1, 1, 1)
tuple2 = ('a', 'a', 'a')
tuple3 = (1, 2, 1, 1)
tuple4 = () # Empty tuple
tuple5 = (5,) # Single-element tuple

print(f"Are all items in {tuple1} the same? {are_all_items_same(tuple1)}")
print(f"Are all items in {tuple2} the same? {are_all_items_same(tuple2)}")
print(f"Are all items in {tuple3} the same? {are_all_items_same(tuple3)}")
print(f"Are all items in {tuple4} the same? {are_all_items_same(tuple4)}")
print(f"Are all items in {tuple5} the same? {are_all_items_same(tuple5)}")