# 4.1 Create and access dictionary elements
my_dict = {
    "name": "Smmruti",
    "age": 20,
    "course": "Engineering"
}

print("Dictionary:", my_dict)
print("Name:", my_dict["name"])

# 4.2 Update dictionary
my_dict["age"] = 20
my_dict["college"] = "MIT"
print("Updated Dictionary:", my_dict)

# 4.3 Removing elements
my_dict.pop("course")
print("After removing 'course':", my_dict)

# 4.4 Merging dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2   # Python 3.9+
print("Merged Dictionary:", merged_dict)
