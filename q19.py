my_tuple = (10, 20, 30, 40, 50)
item_to_remove = 30

# Find the index of the item to remove
try:
    index_to_remove = my_tuple.index(item_to_remove)
    
    # Create a new tuple by concatenating slices
    # Exclude the element at index_to_remove
    new_tuple = my_tuple[:index_to_remove] + my_tuple[index_to_remove+1:]
    
    print(f"Original tuple: {my_tuple}")
    print(f"New tuple after removing {item_to_remove}: {new_tuple}")

except ValueError:
    print(f"Item {item_to_remove} not found in the tuple.")