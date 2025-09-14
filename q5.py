# Define two tuples
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

print(f"Before swapping:")
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")

# Swap the tuples using tuple unpacking
tuple1, tuple2 = tuple2, tuple1

print(f"\nAfter swapping:")
print(f"Tuple 1: {tuple1}")
print(f"Tuple 2: {tuple2}")