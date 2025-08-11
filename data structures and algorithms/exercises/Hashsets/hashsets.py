# Hash sets provide constant-time insertion, retrieval and deletion -> O(1) time
# Hash sets eliminates duplicates

# Defining a hash set
student_ids = set()

# Add elements to the hash set
student_ids.add(123)
student_ids.add(456)
student_ids.add(789)

# Check existence
print(123 in student_ids)
print(111 in student_ids)

# Remove an item
student_ids.remove(123)
print(123 in student_ids) # False

# Creating a copy
new_list = set(["Eggs", "Jams", "Ham"])
new_list_copy = new_list.copy()

print(new_list, new_list_copy)


# Sets can be used in mathematical set ops
def array_intersection(list1, list2):
    set1 = set(list1)
    set2 = set(list2)

    intersection = set1 & set2
    return sorted(list(intersection))


def non_repeating_elements(nums):
    """Function to get non-repeating elements in a given list"""
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)
    
    return list(seen - repeated)


def unique_elements(list1, list2):
    """This is similar to set union - set intersection"""
    set1 = list(list1)
    set2 = list(list2)
    unique_to_1 = sorted(list(set1 - set2))
    unique_to_2 = sorted(list(set2 - set1))
    return (unique_to_1, unique_to_2)