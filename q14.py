# Original tuple
my_tuple = (1, 2, 3)

# Item to add
new_item = 4

# Create a new tuple by concatenating the original tuple with a tuple containing the new item
new_tuple = my_tuple + (new_item,)

print(f"Original tuple: {my_tuple}")
print(f"New tuple after adding an item: {new_tuple}")

# Adding multiple items
another_tuple = ("a", "b")
items_to_add = ("c", "d")
updated_tuple = another_tuple + items_to_add
print(f"Original tuple: {another_tuple}")
print(f"New tuple after adding multiple items: {updated_tuple}")