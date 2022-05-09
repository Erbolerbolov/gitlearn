'''
Полиморфизм это возможность использование один и тот же код для разных типов данных, 
Полиморфизм разное поведение одного и того же метода в разных классах!  
Полиморфизм это способность выполнять действия над обьектом независимо от его типа
                   |||||||||||||Полиформизм    на примере оператора +||||||||||||||

'''

# a = 6
# b = 9
# print(a + b)
# c = '6'
# d = '9'
# print(c + d)
# f = [1,2,3,4,5]
# e = [6,7,8,9]
# print(f + e)


# Функция DIR()
# __add__  завасит в каком классе применяется этот метод!!
# a = 'makers'
# b = 3
# c = [True, 'Bootcamp', 766]
# d = {'makers': 'bootcamp'}
# e = (6,7,8,9)
# f = {False, 'makers', 6, 3, 8}
# print(f'this is string methods: {dir(a)}')
# print(f'this is string methods: {dir(b)}')
# print(f'this is string methods: {dir(c)}')
# print(f'this is string methods: {dir(d)}')
# print(f'this is string methods: {dir(e)}')
# print(f'this is string methods: {dir(f)}')




'''
                          Полиморфизм на примере встроенных методов

'''


# pop() - > list, dict, set!

# list_ = [3,4,5,6]
# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 78, 0}

# list_.pop(1)
# dict_.pop('b')
# set_.pop()

# print(list_)
# print(dict_)
# print(set_)




#update() -> dict, set

# dict_ = dict(a=1, b=2, c=3)
# set_ = {True, 'makers', 78, 0}

# dict_.update(d=4, e=5)
# set_.update({8,0,-1})
# print(dict_)
# print(set_)



'''
                             ИСпользование полиморфизма в своих классах!!!!!


'''


# class Car:
#     def __init__(self, name):
#         self.name= name
    
#     def go(self,destination):
#         print(f'{self.name} is going by car to {destination}')


# class Ship:
#     def __init__(self,name):
#         self.name = name
        
#     def go(self, destination):
#         print(f'{self.name} is going by ship to {destination}')

# class Airplane:
#     def __init__(self,name):
#         self.name =name

#     def go(self, destination):
#         print(f'{self.name} is flying by airplane to {destination}')

# class Train:
#     def __init__(self,name):
#         self.name = name
    
#     def go(self, destination):
#         print(f'{self.name} is going by train to {destination}')









# через Infomixin

# class Infomixin:
#     def info(self):
#         my_class = self.__class__.__name__
#         print(f'i am {my_class}, named {self.name} age {self.age}')





# class Cat(Infomixin):
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

  

#     def make_sound(self):
#         print('meow')

# class Dog(Infomixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    



#     def make_sound(self):
#         print('woof')

# class Duck(Infomixin):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    


#     def make_sound(self):
#         print('kvak')

    
# animal = Dog('tom', 7)
# animal.info()










# class T1:
#     def __init__(self, iterable):
#         self.list = iterable
    
#     def total(self):
#         return sum(self.list)

# class T2:
#     def __init__(self, iterable):
#         self.list = iterable
    
#     def total(self):
#         return len(self.list)

    
# t1 = T1([1,2,3,4,5,6,7])
# t2 = T2([1,2,3,4,5,6,7])
# print(t1.total())
# print(t2.total())


# a  = 'erbosha'
# b = [1,2,3,4,5]
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}    task 1 polimorfizm
# list_ = a, b, c
# for elem in list_:
#     print(len(elem))



# class Dog:
#     def voice():
#         print('Гав')

# class Cat:
#     def voice():
#         print('Мяу')

# to_pet(barsik) 
# to_pet(rex)







# num1 = 5   # int
# num2 = 5   # int
# print(num1 + num2)

# str1 = 'hello'
# str2 = 'Erbol'
# print(str1 + str2)

# print(len('hello'))
# print(len([1,2,3,4,5]))
# print(len({'1': 1, '2': 2}))





# class Animal:

#     pass

# class Cat(Animal):
    
#     def make_sound(self):
#         print('meow')

# class Dog(Animal):
    
#     def make_sound(self):
#         print('gaf')

# class Bird(Animal):
    
#     def make_sound(self):
#         print('чик чирик')


# cat = Cat()
# dog = Dog()
# cats = [Cat() for i in range(10)]
# dogs = [Dog() for i in range(5)]
# birds = [Bird() for i in range(3)]

# cat.make_sound_cat()
# dog.make_sound_dog()


# animals: list = []
# animals.extend(cats)
# animals.extend(dogs)
# animals.extend(birds)


# for animal in animals:
    # if isinstance(animal, Cat):
    #     animal.make_sound_cat()
    # elif isinstance(animal, Dog):
    #     animal.make_sound_dog()
    # else:
    #     animal.make_sound_bird()
    # animal.make_sound()



# class BaseUser:

#     def __str__(self):
#         raise NotImplemented

# class User(BaseUser):
    
#     def __str__(self):
#         return 'i  am basic'
# class VipUser(BaseUser):
#     def __str__(self):
#         return ' iam VIP'

# vip_user = VipUser()
# # print(vip_user)


# from abc import ABC, abstractclassmethod
# from python import get_split_info, password_input_and_check

# class AbstractUser(ABC):

#     @abstractclassmethod
#     def __init__(self) -> None:
#         pass

#     @abstractclassmethod
#     def __str__(self) -> str:
#         pass

#     @abstractclassmethod
#     def get_info(self):
#         pass


# class User(AbstractUser):

#     def __init__(self, fio, age, email):
#         fio = get_split_info(fio)
#         self.surname, self.name, self.last_name = fio[0] , fio[1], fio[-1] 
#         self.age = age
#         self.email = email
    
#     def __str__(self) -> str:
#         return self.name
#     @property
#     def get_info(self):
#         info = {'name': self.name,
#         'surname': self.surname,
#         'last_name': self.last_name,
#         'age': self.age,
#         'email': self.email}
#         return info
    

# class Instagram(User):

#     def __init__(self, fio, age, email, phone):
#         super().__init__(fio, age, email)
#         self.phone = phone
#         self.password = password_input_and_check()
#         self.bot = False
#         self.is_active = False
#         self.active_code = self.generate_active_code
#         self.count_subscribe = 0
#         self.count_subscribes = 0
#         print(self.active_code())


#     def generate_active_code(self):
#         code = self.password[::-1].upper() + self.name + '#@!'
#         return code
    
#     def get_active_code(self):
#         return self.active_code
    
#     def send_activate_code(self, code):
#         if self.get_active_code() == code:
#             self.is_active = True
#         else:
#             raise ValueError('Активационный ключ не совпадает!!')

    
#     def subscribe(self, obj):
#         if self.is_active_():
#             self.count_subscribe = self.count_subscribe + 1
#             obj.subscribes
#         else:
#             raise ValueError('Пользователь не активный ')


#     @property
#     def subscribes(self):
#         self.count_subscribes = self.count_subscribes + 1
#         return self.count_subscribes
    
#     def is_active_(self):
#         return self.is_active

        
#     def __str__(self):
#         return f'{self.name} {self.password}'



    


# class Employee(User):

#     pass

# # Erbol = User('Testov Erbol testovich', 23, 'Erbol@gmail.com')
# # print(Erbol)
# # print(Erbol.get_info)

# Erbol = Instagram('Testov Daria testovich', 25, 'Erbol@gmail.com', '0708989898')
# Erbol.send_activate_code(input('enter active code: '))

# Daria = Instagram('Testov Daria testovich', 25, 'Daria@gmail.com', '0708989898')

# print(Daria.count_subscribes)
# try:

#     Erbol.subscribe(Daria)
# except ValueError as e:
#     print(e)
# print(Erbol.is_active)


# print(Daria.count_subscribes)














# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
    
# class Employee(Person):
#     def __init__(self, work, status):
#         super().__init__(self.name, self.last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'Привет, меня зовут Иван Петров, я работаю в компании {self.work} и копыта на должности {self.status}.'
# class Student(Person):
#     def __init__(self, university, course):
#         super().__init__(self.name, self.last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'Привет, меня зовут Иван Петров, я учусь в {self.university} на {self.course} курсе'

# def get_human_info(self):
#     self.get_info()

# person = Person('Иван', 'Петров')
# employee = Employee('Рога', 'директор')
# student = Student('КГТУ', 3)



# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)
    









# class WhatsApp: 
#     def __init__(self, phone:int):
#         self.phone= phone
    
#     def send(self, text:str):
#         print(f'I am sending a text {text}')
        

        

# class Snapchat:
#     def __init__(self, phone:int):
#         self.phone = phone
    
#     def send(self, image:bool, text:str):
#         if image:
#             print(f'I am sending a text {text} with some image')
#         else:
#             print(f'I am sending a text {text} without image')
        
        

# class Telegram:
#     def __init__(self, phone:int, username:int):
#         self.phone = phone
#         self.username = username

#     def send(self, voice_message:str):
#         print(f'I am sending a voice message {voice_message}')


# obj1 = WhatsApp(934394394939439)
# obj2 = Snapchat(324242423)
# obj3 = Telegram(324324242, 324242)
# objcc = Snapchat(324243242)

# obj1.send('Hello makers!!!!1')
# obj2.send(True, 'erbosha')
# obj3.send('fdsfsdfsdf')
# objcc.send(False, 'kakosikdak')








# class A:
#     def count(self, word:str):
#         self.count = 0
#         vowels =['a', 'o', 'y', 'i', 'e', 'o', 'u']
#         for i in word:
#             if i in vowels:
#                 self.count += 1
#             return self.count

# class B:
#     def count(self, word:str):
#         self.count = 0
#         sogl = ['b', 's', 'd', 'f', 'g', 'w', 'x', 'p', 'n',]
#         for i in word:
#             if i in sogl:
#                 self.count += 1
#             return self.count

# erbol = A()
# erbol1 = B()

# print(erbol.count('erbolerbolov'))
# print(erbol1.count('azhybekovErbol'))








# class ToDo:    
#     instances ={}
#     def __init__(self):
#         pass
        
#     def give_priority(self, priority:int, task:str):
#         self.priority=priority
#         self.task=task
#         ToDo.instances.update({self.priority:self.task})
#     def list_of_tasks(self):
#         sorted_task_list=[]
#         def take_key(elem):
#             return elem[0]
#         sorted_task_list = sorted(ToDo.instances.items(), key=take_key)
#         return sorted_task_list ## плохо поняла , но работает
       
# task1=ToDo()
# task1.give_priority(3,'сходить в кино')
# task2=ToDo()
# task2.give_priority(1,'сделать домашку')
# task3=ToDo()
# task3.give_priority(2,'выгулять собаку')
# print(ToDo.instances)
# print(task3.list_of_tasks())














# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#        print(self.pi * self.radius ** 2)  
    
    
# circle = Circle(2)
# circle.color = 'Красный'
# circle.get_area()





# class Dog:
#     def voice():
#         print('Гав')

# class Cat:
#     def voice():
#         print('Мяу')
    

# barsik = Dog()
# rex = Cat()
# def to_pet():
    # to_pet(barsik)
    # to_pet(rex)





# class Dog:
#     def voice():
#         print('Гав')

# class Cat:
#     def voice():
#         print('Мяу')

# to_pet(barsik) 
# to_pet(rex)





# class Phonebook:














# class Phone:

#     def __init__(self, name, last_name,number):
#         self.name = name
#         self.last_name = last_name
#         self.number = number

#     def get_info(self):
#         print(f"Контакт:{self.name} {self.last_name}, телефон: {self.number}")



# person = Phone('Иван', 'Петров', 'v')
# person.get_info()










# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
    
# class Employee(Person):
#     def __init__(self, work, status):
#         super().__init__(self.name, self.last_name)
#         self.work = work
#         self.status = status
#     def get_info(self):
#         return f'Привет, меня зовут Иван Петров, я работаю в компании {self.work} и копыта на должности {self.status}.'
# class Student(Person):
#     def __init__(self, university, course):
#         super().__init__(self.name, self.last_name)
#         self.university = university
#         self.course = course
#     def get_info(self):
#         return f'Привет, меня зовут Иван Петров, я учусь в {self.university} на {self.course} курсе'

# def get_human_info(self):
#     self.get_info()

# person = Person('Иван', 'Петров')
# employee = Employee('Рога', 'директор')
# student = Student('КГТУ', 3)



# class Cat:
      
#     def voice(self):
#         print("Мяу")

# class Dog:
#     def voice(self):
#         print("Гав")
      
# cat = Cat()
# dog = Dog()

# cat.voice()
# dog.voice()








def dec_(func):
    def wrapper(name):
        print(f'Вызываю функцию {name}')
        func(name)
        print(f'Вызов функции {name} прошел успешно')
    return wrapper

@dec_
def sand(name):
    print(f' {name} ')

sand('Snow')




# def decorator(func):
#     def wrapper(name):
#         print(f'Вызываю функцию {name}')
#         func(name)
#         print(f'Вызов функции {name} прошёл успешно')
#     return wrapper

# @decorator
# def greeting(name):
#   print(f'Hello {name.capitalize()}')

# greeting('erbol')