def copy_specific_elements(source_table, new_table_name, condition_func):
    """
    Copies specific elements from a source table to a new table based on a condition.

    Args:
        source_table (list of dict): The list of dictionaries representing the source table.
        new_table_name (str): The name for the new table (for demonstration purposes,
                              this example creates a new list, not a named table).
        condition_func (function): A function that takes a row (dictionary) as input
                                   and returns True if the row should be copied, False otherwise.

    Returns:
        list of dict: The new table containing the copied elements.
    """
    new_table = []
    for row in source_table:
        if condition_func(row):
            new_table.append(row.copy())  # Use .copy() to create a shallow copy of the dictionary
    return new_table

# Example Usage:

# Source table (list of dictionaries)
employees = [
    {"id": 1, "name": "Alice", "department": "HR", "salary": 60000},
    {"id": 2, "name": "Bob", "department": "IT", "salary": 75000},
    {"id": 3, "name": "Charlie", "department": "HR", "salary": 62000},
    {"id": 4, "name": "David", "department": "Marketing", "salary": 58000},
    {"id": 5, "name": "Eve", "department": "IT", "salary": 80000},
]

# 1. Copy all employees from the 'HR' department
def is_hr_employee(employee):
    return employee["department"] == "HR"

hr_employees_table = copy_specific_elements(employees, "HR_Employees", is_hr_employee)
print("HR Employees Table:")
for employee in hr_employees_table:
    print(employee)

print("\n")

# 2. Copy employees with a salary greater than 70000
def is_high_earner(employee):
    return employee["salary"] > 70000

high_earner_employees_table = copy_specific_elements(employees, "High_Earners", is_high_earner)
print("High Earner Employees Table:")
for employee in high_earner_employees_table:
    print(employee)