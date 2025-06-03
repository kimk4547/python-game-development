#list is a data structure that is non-homogeneous, mutable.
#dictionary is a data structure, it is also non-homogeneous.
student_list = ["Jane", 12, "nowhere street", 480, 89.78]
print(student_list[1])
#dictionary stores data in key-value pairs
student_dict = {
    "name": "Jane",
    "age": 12,
    "address": "nowhere street",
    "marks" : 480,
    "percentage": 89.78
}
#here name is the key and "jane is the value "
#accessing the value from dictionary
print(student_dict['name'])
print(student_dict)
# get the values from the dictionary
print (student_dict.values())
#get the keys
print(student_dict.keys())
#let us use loop
for key in student_dict.keys():
    print(key, student_dict[key])

#check if the key-value is present in the dictionary or not
if "grade" in student_dict:
    print(student_dict["grade"])
else:
    print("key does not exist")
#let us add key-value in the existing dictionary.
student_dict["grade"] = "A"
print(student_dict)
#delete the key-value pair
del(student_dict["grade"])
print(student_dict)
#change the value of a key
student_dict["address"] = "anywhere street park avenue"
print(student_dict)
#nested dictionary
classroom = {}
    "Jane" :{
        'age': 12,
        'marks': 480,
        'grade' : '
},
'John': {
    'age': 14,
    'marks': 570,
    'grade': 'A+'
 }

