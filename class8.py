# 🚀 *What You'll Learn:*
# - 📚 Basics of Python dictionaries
# - 🛠️ How to create, access, and manipulate dictionary data
# - 🧠 In-depth explanations of various dictionary methods with code examples

# 👨‍💻 *Follow Along with the Code:*

# *Creating a Dictionary:*
# ```python
# my_dict = {'apple': 5, 'banana': 3}
# print(my_dict)  # Output: {'apple': 5, 'banana': 3}
# ```

# *Accessing Values:*
# ```python
# value = my_dict['apple']
# print(value)  # Output: 5
# ```

# *Adding Key-Value Pairs:*
# ```python
# my_dict['cherry'] = 7
# print(my_dict)  # Output: {'apple': 5, 'banana': 3, 'cherry': 7}
# ```

# 🛠️ *Must-Know Dictionary Methods:*

# 1. *clear:* Removes all items.
#    ```python
#    my_dict.clear()
#    ```
# 2. *copy:* Creates a shallow copy.
#    ```python
#    copy_dict = my_dict.copy()
#    ```
# 3. *fromkeys:* Creates a new dictionary from a sequence of keys.
#    ```python
#    new_dict = dict.fromkeys(['apple', 'banana'], 0)
#    ```
# 4. *get:* Retrieves the value for a given key.
#    ```python
#    value = my_dict.get('apple', 'Not Found')
#    ```
# 5. *items:* Returns a view of all key-value pairs.
#    ```python
#    items = my_dict.items()
#    ```
# 6. *keys:* Returns all the keys.
#    ```python
#    keys = my_dict.keys()
#    ```
# 7. *pop:* Removes an item by key.
#    ```python
#    my_dict.pop('apple')
#    ```
# 8. *popitem:* Removes the last key-value pair.
#    ```python
#    my_dict.popitem()
#    ```
# 9. *setdefault:* Gets the value of a key, and if not present, sets a default value.
#    ```python
#    value = my_dict.setdefault('banana', 6)
#    ```
# 10. *update:* Updates the dictionary.
#     ```python
#     my_dict.update({'banana': 4})
#     ```
# 11. *values:* Returns all the values.
#     ```python
#     values = my_dict.values()
#     ```

# 🔥 *Pro Tips:*
# - Use `get` to avoid KeyError when accessing non-existent keys.
# - Utilize `update` to merge two dictionaries easily.
# - Remember that dictionaries are unordered collections of data (until Python 3.7, where they are insertion ordered).

# 💡 *Conclusion:*
# Dictionaries are a powerful feature in Python, perfect for handling key-value paired data. Mastering them can significantly enhance your coding efficiency.
