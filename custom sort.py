def sort_dicts_by_key(dicts, key):
    return sorted(dicts, key=lambda x: x[key])

# Example usage:
list_of_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

sorted_list = sort_dicts_by_key(list_of_dicts, "age")
print(sorted_list)
# Output: [{'name': 'Bob', 'age': 20}, {'name': 'Alice', 'age': 25}, {'name': 'Charlie', 'age': 30}]