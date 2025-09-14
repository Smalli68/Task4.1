def sort_tuple_of_tuples_by_second_item(input_tuple_of_tuples):
  """
  Sorts a tuple of tuples based on the second item of each inner tuple.

  Args:
    input_tuple_of_tuples: A tuple containing inner tuples, where each inner tuple
                           has at least two elements.

  Returns:
    A new tuple of tuples, sorted by the second item of the inner tuples.
  """
  # Convert the tuple of tuples to a list of tuples to allow sorting
  list_of_tuples = list(input_tuple_of_tuples)

  # Sort the list using a lambda function to specify the sorting key
  list_of_tuples.sort(key=lambda x: x[1])

  # Convert the sorted list back to a tuple
  sorted_tuple_of_tuples = tuple(list_of_tuples)
  return sorted_tuple_of_tuples

# Example usage:
data = (('A', 23), ('B', 37), ('C', 11), ('D', 29))
sorted_data = sort_tuple_of_tuples_by_second_item(data)
print(sorted_data)