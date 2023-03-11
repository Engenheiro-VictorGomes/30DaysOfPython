# 10. Delete one of the items in the dictionary
student = {
            'first_name':'ValueFirstName',
            'last_name':'',
            'gender':'',
            'age':'',
            'marital_status':'',
            'skills':[],
            'country':'',
            'city':'',
            'address':''
        }

# removing the last item
student.popitem()

# Return an specific value, and delete it from the dict. Exception if the key doesn´t exist
firstNameValue = student.pop('first_name')
print(firstNameValue)

# Return an specific value, and delete it from the dict. Default value if the key doesn´t exist
firstNameValue = student.pop('first_name2', 'DefaultValue')
print(firstNameValue)

# removing specific key. Exception if key doesn´t exist
del student['gender']