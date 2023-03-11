# 6. Modify the skills values by adding one or two skills
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

student['skills'].append('Skill 1')
student['skills'].append('Skill 2')
print(student['skills'])