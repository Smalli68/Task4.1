def find_repeated_items(input_tuple):
    """
    Finds and returns a set of repeated items in a given tuple.

    Args:
        input_tuple: The tuple to search for repeated items.

    Returns:
        A set containing the repeated items from the input tuple.
    """
    seen = set()
    repeated_items = set()

    for item in input_tuple:
        if item in seen:
            repeated_items.add(item)
        else:
            seen.add(item)
    return repeated_items

# Example usage:
my_tuple = (1, 2, 3, 2, 4, 5, 1, 6, 3, 7, 8, 8)
repeated = find_repeated_items(my_tuple)
print(f"The original tuple: {my_tuple}")
print(f"The repeated items in the tuple are: {repeated}")

another_tuple = ('apple', 'banana', 'orange', 'apple', 'grape', 'banana')
repeated_fruits = find_repeated_items(another_tuple)
print(f"\nThe original tuple: {another_tuple}")
print(f"The repeated items in the tuple are: {repeated_fruits}")