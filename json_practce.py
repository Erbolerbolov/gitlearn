'''

dump(), dumps()

# '''

# import json 

# info = {
#     'name': 'Alice',
#     'age': 79,
#     'book':'Chamber of Secrets'
# }


# print(type(info))

# with open('info.json', 'w') as my_file:
#     json.dump(info, my_file)


# json_object = json.dumps(info)
# print(json_object) 












'''
load(), loads()

'''


# import json



# with open('info.json') as my_file:
#     pythone_object = json.load(my_file)
#     print(type(pythone_object))


# pythone_object['name'] = 'Erbol'
# print(pythone_object)


# with open('info.json', 'w') as my_file:
#     json.dump(pythone_object, my_file)





# json_str = '{"name": "Alice", "age": 79, "book": "Chamber of Secrets"}'
# python_object = json.loads(json_str)
# print(json_str)
# print(python_object)
# print(type(python_object))
# python_object.update({'color': 'yellow'})
# print(python_object)


# import json

# with open('HarryPotterBooks.json') as my_file:
#     dictionary = json.load(my_file)
#     data = dictionary['books']
#     for book in data:
#         book['author'] = 'J.K.Rowling'

#     # print(dictionary)

# with open('HarryPotteBooks.json', 'w') as my_file:
#     json.dump(dictionary, my_file)







# TASK 1

# import json

# with open('task1.json', 'r') as my_file:
#     python_obj = json.load(my_file)
# with open('task1.py', 'w') as my_file:
#     my_file.write(str(python_obj))
    
    



    
'''
import json
JSON - javascript object natation


'''

'''
dump | dumps
load | loads



Python              JSON
dict                object
list, tuple          array
str                  string
int                     integer
float                   float
True/False               true/False



'''
# import json


# language = {
#     "id: 0": {
#         "language": "Python",
#         "weeks": "13"
#     },
#     "id: 1": {
#         "language": "JavaScript",
#         "weeks": 13
#     }
# }

# groups = {
#     "id: 1":{
#         "title": "Python19",
#         "nickname": 'Zmeika PEPA',
#         "lqnguage": [0]
#     }
# }

# obj = {
#     "name": "Umida",
#     "gender": "Female",
#     "email": "Umida@gmail.com",
#     "groups": [1]

# }

# with open("obj_info.json", mode="w") as file:
#     json.dump(obj, file, indent=4)


# метод dumps!

# json_object = json.dumps(obj)
# # print(json_object)
# # print(type(json_object))

# python_object = json.loads(json_object)
# print(python_object["name"])
# print(type(python_object))



# with open("obj_info.json", 'r') as file:
#     print(json.load(file)["gender"])




import re
from urllib import response
import requests
import json


URL = "https://jsonplaceholder.typicode.com/posts"


def get_responce(url: str):
    response = requests.get(url)
    return response.text  #response.json()

def load_python_object(response: str):
    return json.loads(response)



response = get_responce(URL)
python_object = load_python_object(response)
# print(python_object[1]["body"])

# for obj in python_object:
#     print(obj["userId"])


class Post:

    def __init__(self, *args, **kwargs):
        self.__dict__.update(*args, **kwargs)


    def get_info(self):
        return f'{self.title} {self.body}'

    def get_id(self):
        return self.id

obj1 = python_object[0]
post = Post(obj1)
# print(post.__dict__)
print(post.get_info())

##test to check commit on branch
