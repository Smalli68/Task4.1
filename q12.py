# Create a tuple named 'bull_characteristics' to store various data types
bull_characteristics = (
    "Strong",          # String: representing a characteristic
    1500,              # Integer: representing weight in kg
    True,              # Boolean: indicating if it's a male
    4.5,               # Float: representing height in feet
    ["Horned", "Muscular"], # List: representing physical attributes
    {"color": "brown", "breed": "Angus"} # Dictionary: representing more specific details
)

# Print the entire tuple
print("Bull Characteristics Tuple:")
print(bull_characteristics)

# Print each element and its data type
print("\nIndividual Characteristics and their Data Types:")
for item in bull_characteristics:
    print(f"Value: {item}, Type: {type(item)}")