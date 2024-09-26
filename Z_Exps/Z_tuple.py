student_data = (
    ("Alice", 18, (90, 85, 95)),
    ("Bob", 17, (75, 80, 90)),
    ("Charlie", 19, (88, 92, 85))
)

for student in student_data:
    print(student[0])
    print(student[1])
    print(student[2])

value = student_data[2][2][2]
print(value)

#student_data[2][2][2] = 80
# new_value = student_data[2][2][2]
# print(new_value)

def my_function():
    return (101,'Sanjeevu','Male')

id,name,_ = my_function()
print(f'id:{id} name:{name}')