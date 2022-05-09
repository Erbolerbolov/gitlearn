'''

ДЕКОРАТОР - просто функция которая оборачивает другую функцию неизменяя ее (функция которая расширяет функционал другой функции не меняя ее код!)

'''
from datetime import datetime
from multiprocessing.connection import wait
from operator import truediv
import re
import requests

# def func():
    
#     def func2():
#         return 'привет я функция func2'
#     return func2
# some_func = func()
# # print(some_func)
# print(some_func())


# def func(func):
#     print('вызов функции func()')
#     func()

# def func2():
#     print('вызов функции func2()')
# func(func2)


# def decorator(func):  # ФУНКЦИЯ ДЕКОРАТОР она принимает в качестве аргумента функцию

#     def wrapper():  # Функция обертка
#         print('я код который срабол до вызова функции')
#         func()
#         print('я код который сработал после вызова функции')


#     return wrapper # Обязательно нужно возвращать !!

# def func():
#     print('я функция которую вызвали')

# some_func = decorator(func)() # decorator(func)()





# def bread(func):
#     def wrapper():
#         print('---Хлеб---')
#         func()
#         print('---Хлеб---')
#     return wrapper

# def ingrediients(func):
#     def wrapper():
#         print('---Лук---')
#         func()
#         print('---листсалат---')
#     return wrapper

# @bread
# @ingrediients   #декораторы
# def sandwich():
#     print('---котлета---')

# sandwich()


# def decorator(func):
#     def wrapper(a, b):                      #  ОНа принимает аргуменнты вызываемой функции 
#         print('это сложение двух чисел')
#         print(func(a, b))
#     return wrapper


# @decorator
# def  sum_to(a, b):
#     return a + b
# sum_to(5,5)





# def benchmark(func):
#     from time import time 
#     def wrapper():
#         start = time()
#         func()
#         end = time()

#         print(f'Функция отработала за {end-start} секунд')
#     return wrapper
# @benchmark
# def get_google():
#     requests.get('hhtps://google.com')

# # get_google()
# @benchmark
# def range_hundred():
#     for i in range(10000000):
#         pass

# def get_youtube
# range_hundred()





# def check_time(func):
#     from time import time

#     def wrapper(**kwargs):
#         start = time()
#         func(**kwargs)
#         end = time()
#         print(f'Функция отработала за {end-start} секунд')
        

#     return wrapper 

# @check_time
# def get_response(**kwargs):
#     print(kwargs)
#     import requests
#     requests.get(url=kwargs['url'])

# get_response(url='https://youtube.com')
# get_response(url='https://oc.kg')
# get_response(url='https://ts.kg')






# def decorator(func):
    
#     def wrapper(*args, **kwargs):

#         print(f'это кортеж {args}')
#         print(f'это словарь{kwargs}')
#         func(*args, **kwargs)
#     return wrapper
# @decorator
# def func():
#     print("Обычная функция без аргументов")
# @decorator
# def func1(url):
#     print('С параметром обязательным')
# @decorator
# def func2(url, method):
#     print('С параметром обязательными')

# func()
# func1('https://google.com')
# func2(url='https://youtube.com', method='get')




# def decorator_main():

#     print('я первый декоратор')

#     def decorator(func):
#         print(('Я просто декоратор'))
#         def wrapper():
#             print('я функция обертка')
#             func()
#         return wrapper
#     return decorator

# @decorator_main()
# def func():
#     print('я обычная функция')

# func()

# from 








# def check_email(emails: list) -> bool:

#     def decorator(func):

#         def wrapper(email: str):

#             if any(email.endswith(email1) for email1 in emails):
#                 return True
#             return False

#         return wrapper

#     return decorator


# @check_email(['@gmail.com', '@yandex.ru'])
# def is_email(email: str) -> bool:
#     '''
#     Функция проверяет на правильность email
#     '''
#     if '@' in email:
#         return True
#     return False
# email = input('enter email:  ')
# if is_email(email=email):
#     print('ваш email четко подходит!')
# else:
#     print('Неправильный email!!!!!')









# def hello_makers():
#       print('Hello, Makers!')

# # хранить функции в переменных 
# makers = hello_makers
# print(id(makers))
# print(id(hello_makers))

# Определить функции внутри другой функции 

# def outer_func():
#     def inner_func():
#         print('Hello, Makers')
#     inner_func()

# outer_func()

# Передавать функции в качестве аргумента и возвращать их из других функции

# def main_func(func):
#     print(f'я получила функцию{func} в качестве аргумента')
#     func()
#     return func

# def hello_makers():
#     print('Hello, Makers!')


# print(main_func(hello_makers))


#Декораторы 

# def func1():
#     print('im coalled inside other function')

# def func2(func):
#     print('ill do somthing before func calling')
#     func()
# def func3():
#     print('hello, naker1!!!')
# func2(func3)



# def decorator(func):
#     print('я функция декоратор')
#     def wrapper():
#         print('я функция обертка')
#         print('вызываем обернутую функцию')
#         func()
#         print('выхожу из обертки')
#         return func
        
#     return wrapper

# @ 
# @decorator
# # def hello_makers():
# #     print('hello, makers!')

# def hello_bootcamp():
#     print('this is Bootcamp!')
# hello_bootcamp()



# def check_password(func):
#     def wrapper(parameter):
#         return func(parameter).strip()
#     return wrapper

    
# @check_password
# def get_password(password):
#     return password


# password = input('Enter passwrod: ')
# print(get_password(password))



# def func1():
#     print('im called insdide other function')

# def func2(func):
#     print('ill do something func calling')
#     func()
# def func3():
#     print('hello makers!!!!!1')

# func2(func2)

# def decorator(func):
#     print('я функция декоратор')
#     def wrapper():
#         print('я функция обертка')
#         print('вызываем обернутую функцию')
#         func()
#         print('выхожу из обертки')
#         return func
#     return wrapper

# @
# @decorator
# def hello_makers():
#     print('hello, makers!')
# @decorator
# def hello_bootcamp():
#     print('this is bootcamp')

# hello_bootcamp()





# def check_password(func):
#     def wrapper(parametr):
#         return func(parametr).strip()
#     return wrapper

# @check_password
# def get_info(param: str) -> str:
#     return param

# param= input('enter password: ')
# print(get_info(param))




# def bread(func):
#     def wrapper(filler):
#         print('</---\>')
#         func(filler)
#         print('</___\>')
#     return wrapper

# def ingredients(func):
#     def wrapper(filler):
#         print('#tomato')
#         func(filler)
#         print('--slad--')
#     return wrapper

# @bread
# @ingredients
# def get_sandwich(filler):
#     print(filler)
# get_sandwich('--ham--')








# from datetime import datetime
# def func_start_time(func):
#     date = datetime.now()
#     def wrapper():
#         print(f"Функция запущена {date.strftime('%d.%m.%Y %H:%M')}")
#         func()
#     return wrapper
# @func_start_time
# def func():
#     print('Hello world')                    #Task 2
# func()






# def make_bold(func):
#     def wrapper():
#         return (f'<b>{func()}</b>')
#     return wrapper
    
    


# def make_italic(func):
#     def wrapper():
#         return (f'<i>{func()}</i>')
#     return wrapper
    


# def make_underline(func):
#     def wrapper():
#         return (f'<u>{func()}</u>')             taks 3
#     return wrapper

# def hello():
#     def wrapper():
#         return 'Hello world'

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'
 
# print(hello())






# import time
# def benchmark(func):
#     def wrapper():
#         print(time.time())
#     return wrapper

# @benchmark 
# def fetch_webpage(): 
#     import requests 
#     webpage = 
# requests.get('https://google.com')


# users = {'username': 2, 'password': 6, }

# def validate_password(func):
#     def wrapper():
#         for i in users.items():
#             if i == 'username':
#                 print('hello brat')
#             if i != 'username':
#                 print('Username is not defined')
#             else:
#                 print('Password is invalid')
#             func()
#         return wrapper
#             print(validate_password())












# users = {'Erlan': '012345', 'Erlan1': 'fasdf1'}

# def validate_password(func):
#     def wrapper(username,password):
#         try:
#             passw=users[username]
#             if passw==password:
#                 func(username,password)
#             else:
#                 print('Password is invalid')
#         except:
#             print('Username is not defined')
#     return wrapper
            

            
# @validate_password
# def login(username, password):
#         print(f'Welcome, {username}')

# login('Erlan', '012345')




# def is_admin(func):
#     def wrapper(user):
#         use = user
#         if use== user:
#             print('Доступ разрешен john133')

#         else:
#             print('Доступ запрещен john133')
#     return wrapper
            


# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})













# from operator import itemgetter
# def sort_names(func):
#     def wrapper(person):
#         person=sorted(person,key=itemgetter(2))
#         return func(person)
#     return wrapper
# @sort_names
# def prefix_name(person):
#     return ["Mr. "+human[0]+' '+human[1] if human[-1]=='M' else "Ms. "+human[0]+' '+human[1] for human in person]
# print(prefix_name([('Leo', 'Nimoy', 40, 'M'),
#       ('Carrie', 'Fisher', 35, 'F'),
#       ('Harrison', 'Ford', 38, 'M')]))




# def check_password(func):
#     def wrapper(parametr):
#         return func(parametr).strip()
#     return wrapper

# @check_password
# def get_info(param: str) -> str:
#     return param

# param= input('enter password: ')
# print(get_info(param))


# def timeit(func):
#     def wrapper():
#         start = datetime.now()
#         result = func()
#         print(datetime.now)- start)
    

        

#     return wrapper





# def onee():
#     l = []
#     for i in range(60):
#         if i % 2 == 0:
#             l.append(i)
#     return l


# def two():
#     l = [x for x in range(30) if x % 2 == 0]
#     return l


# l1 = onee()
# l2 = two()
# print(l1)
# print(l2)









class Phone:
    def __init__(self, name, last_name, phone):
        self.name = name
        self.last_name = last_name
        self.phone = phone
    
    def get_info(self):
        print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')

contact = Phone()
contact.get_info()

