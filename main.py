#   Questions

# Basic Operations

# 1.	Create a dictionary student with keys: name, age, and grade. Assign them appropriate values.


# student = {
#     "name": "Ali Khan",
#     "age": 16,
#     "grade": "A"
# }

# print(student)
   

# 2.	Access the value of the key grade in the student dictionary.


# student = {
#     "name": "Ali Khan",
#     "age": 16,
#     "grade": "A"
# }


# print(student["grade"])
    


# 3.	Add a new key city to the student dictionary and set its value to "New York".

# student = {
#     "name": "Ali Khan",
#     "age": 16,
#     "grade": "A"
# }

# student["city"] = "New York"
# print(student)

# {
#     "name": "Ali Khan",
#     "age": 16,
#     "grade": "A",
#     "city": "New York"
# }



# 4.	Update the value of the age key in the student dictionary to 20.


# student = {
#     "name": "Ali Khan",
#     "age": 16,
#     "grade": "A",
#     "city": "New York"
# }


# student["age"] = 20


# print(student)


# 5.	Remove the key city from the student dictionary.


# student = {
#     "name": "Ali Khan",
#     "age": 16,
#     "grade": "A",
#     "city": "New York"
# }


# student["age"] = 20


# print(student)


# Iterating through Dictionaries
# 6.	Iterate through the dictionary student and print all keys.
# Example dictionary
# student = {
#     "name": "John Doe",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8
# }


# for key in student:
#     print(key)




# 7.	Iterate through the dictionary student and print all values.

# student = {
#     "name": "John Doe",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8
# }


# for value in student.values():
#     print(value)


# 8.	Iterate through the dictionary student and print all key-value pairs in the format key: value.

# student = {
#     "name": "John Doe",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8
# }


# for key, value in student.items():
#     print(f"{key}: {value}")


# 9.	Check if the key grade exists in the student dictionary and print True or False.



# student = {
#     "name": "John Doe",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8
# }


# key_exists = "grade" in student
# print(key_exists)



# 10.	Count the total number of keys in the student dictionary.



# student = {
#     "name": "John Doe",
#     "age": 20,
#     "major": "Computer Science",
#     "gpa": 3.8
# }


# total_keys = len(student)
# print(total_keys)


# Advanced Dictionary Usage

# 11.	Merge the following two dictionaries and print the result:
# 12.	dict1 = {'a': 1, 'b': 2}  
# dict2 = {'c': 3, 'd': 4}  

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}


# dict1.update(dict2)
# print(dict1)



# 13.	Create a dictionary from a list of tuples: [('name', 'Alice'), ('age', 25), ('city', 'Paris')].

# data = [('name', 'Alice'), ('age', 25), ('city', 'Paris')]


# dictionary = dict(data)


# print(dictionary)


# 14.	Sort the keys of the dictionary {'z': 1, 'a': 2, 'c': 3} in ascending order and print the sorted dictionary.


# data = {'z': 1, 'a': 2, 'c': 3}


# sorted_dict = {key: data[key] for key in sorted(data)}


# print(sorted_dict)


# 15.	Reverse the dictionary {'a': 1, 'b': 2, 'c': 3} so that keys become values and values become keys.


# data = {'a': 1, 'b': 2, 'c': 3}


# reversed_dict = {value: key for key, value in data.items()}


# print(reversed_dict)



# 16.	Write a Python function to check if two dictionaries are identical (contain the same key-value pairs).


# def are_dicts_identical(dict1, dict2):
#     """
#     Check if two dictionaries are identical.

#     Parameters:
#         dict1 (dict): The first dictionary.
#         dict2 (dict): The second dictionary.

#     Returns:
#         bool: True if the dictionaries are identical, False otherwise.
#     """
#     return dict1 == dict2

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 1, 'b': 2, 'c': 3}
# dict3 = {'a': 1, 'b': 2, 'c': 4}

# print(are_dicts_identical(dict1, dict2))  
# print(are_dicts_identical(dict1, dict3))  




# Nested Dictionaries


# 16.	Create a nested dictionary to represent the following data:
# 17.	Person:  
# 18.	  Name: John  
# 19.	  Age: 30  
# 20.	  Address:  
# 21.	    Street: 123 Elm St  
# 22.	    City: Boston  
# 23.	Access the value of the City key in the nested dictionary from the previous question.
# 24.	Add a new key Phone to the nested dictionary with the value "123-456-7890".
# 25.	Delete the Address key from the nested dictionary.
# 26.	Iterate through all the keys in the outermost level of the nested dictionary and print them.

# person = {
#     "Name": "John",
#     "Age": 30,
#     "Address": {
#         "Street": "123 Elm St",
#         "City": "Boston"
#     }
# }


# print(person)



# # 	Access the value of the City key in the nested dictionary from the previous question.

# city = person["Address"]["City"]


# print(city)



# # Adding a new key 'Phone' to the dictionary
# person["Phone"] = "123-456-7890"


# print(person)




# # Deleting the 'Address' key
# del person["Address"]

# print(person)



# # Iterating through the keys at the outermost level
# for key in person:
#     print(key)
