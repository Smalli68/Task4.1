# Example with simple tuples
tuple1 = (1, 2)
tuple2 = (3, 4)
nested_tuple = (tuple1, tuple2)
print(f"Concatenated simple tuples to nested: {nested_tuple}")

# Example with already nested tuples
nested_tuple1 = ((1, 2), (3, 4))
nested_tuple2 = ((5, 6), (7, 8))
combined_nested_tuple = nested_tuple1 + nested_tuple2
print(f"Concatenated nested tuples: {combined_nested_tuple}")
