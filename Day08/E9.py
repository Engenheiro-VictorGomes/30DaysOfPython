# 9. Change the dictionary to a list of tuples using items() method
student = {
            'first_name':'',
            'last_name':'',
            'gender':'',
            'age':'',
            'marital_status':'',
            'skills':[],
            'country':'',
            'city':'',
            'address':''
        }
studentTp = student.items()
studentTp = list(studentTp)
print(studentTp)
print(f"It is a {type(studentTp)} of {type(studentTp[0])}")
