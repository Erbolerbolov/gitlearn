# class SomeClass:             создание класса
#     pass




# class A:
#     pass

# a = A()      #создали обьект класса, instance, object
# print(isinstance(a, A))



#class int:
    # свойства класса ......

#class str:
    # свойства ..... 

#class list:
    #свойства !!!!

# a = 4
# class B:
#     pass
# print(type(B))





# a = 5
# print(type(a))

# b = 'makers'
# print(type(b))


# c = [1,2,3,4,5]
# print(type(c))




# im1

# class Dog:
#     owner = 'John'
    

#     def __init__(self, name, age):
#         self.name = name                   #атрибуты экземпляра класса
#         self.age = age
#     def __str__(self):
#         return f'{self.name}, {self.age}'
    
#     def bark(self):
#         print('SalamAleikum')
    

#     def dog_info(self):
#         return f'this is {self.name}, he is {self.age} yesrs old'
    
#     def birthday(self, cake):
#         self.age += 1
#         self.cake = cake
#         return f'{self.name} is  age {self.age} now'
    

#     def friends(self, friend):
#         self.friend = friend
#         friend.friend = self
    

# dog1 = Dog(name='Rex', age=3)
# dog2 = Dog(name='Bobik', age=2)
# dog3 = Dog(name='Oreo', age=1)

# dog1.friends(dog2)
# print(dog1.friend.age)
# print(dog2.friend.name)
# dog3.owner = 'Erbol'                 #<<<<<<<---- через обьект класса можно обратиться атрибуту и поменять значение !!
# dog1.name = 'Tuzik'
# print(dog1.birthday('kulikov'))
# print(dog1.cake)
# print(dog2.birthday('miasnoy'))
# print(dog2.cake)
# dog1.food = 'meat'
# print(dog2.name)
# print(dog1.food)
# dog1.bark()
# dog2.bark()
# dog3.bark()
# dog1.eat()
# print(dog2.dog_info())
# print(dog1.owner)
# print(dog2.owner)
# print(dog3.owner)





# class Rectangle:

#     default_color = 'red'

#     def __init__(self, width, length):
#         self.width = width
#         self.lenght = length
    
#     def area(self):
#         return self.width * self.lenght
# rec1 = Rectangle(4, 6)
# rec2 = Rectangle(2, 7)
# rec2.default_color = 'kyzil'
# print(rec1.default_color)
# print(rec1.width)
# print(rec2.default_color)




# class Car:

#     car_count = 0

#     def __init__(self):
#         Car.car_count += 1

# car1 = Car()
# print(Car.car_count)
# car2 = Car()
# car3 = Car()
# car4 = Car()






'''

ООП  это просто парадигма програмирования 
это просто подход к написанию кода 
класс 
атрибуты класса
методы класса 
экземпляры(обьекты)   класса
атрибуты экземпляра класса 



magic methods (__init__)



Есть понятия Конструктор(__new__, __init__) и Деструктор (__del__)




ПРИНЦИПЫ ООП
основы три принципа ООП ( НАСЛЕДОВАНИЕ, ПОЛИМАОРФИЗМ, ИНКАПСУЛЯЦИЯ)
АССОЦАЦИИ (Агрегация и Композиция)
Абстракции
'''


# class People(object):... class People:... class People():....





# from inspect import _Object


# class Bestprice:...    # CamleCase

# def find_text():... # SnakeCase'



#любой класс наследуется от экземпляра object!

# object ->  Object(type)


# print(isinstance(str, object))











# class People:            # это класс People 

#     head = 'Голова'       # атрибуты класса
#     arms = 'руки'         # # атрибуты класса
#     national = 'Kyrgyz'



# def __init__(self, name) -> None:    #Ссылка на экземпляр класса 
#     self.name = name
         




# Aktan = People('Aktan')  # экземпляром класса People
# Aktan.name = 'Aktan'

# num = int(5)
# print((num))

# print(Aktan.arms)          # обрщение к атриботам класса
# print(Aktan.head)

# Erlan = People('Erlan')
# Erlan.national = 'Russian'
# # print(Erlan.national)
# # 
# Victor = People('viktor')
# print(Victor.national)
 


# num = int()
# print(type(num))
# print(type(Victor))








# class Animal:
#     arms = 4              # атрибут класса
    
#     def __init__(self, name, age, animal_type):
#         # конструктор инициализатор обьекта
#         self.name = name
#         self.age = age
#         self.animal_type = animal_type
#     def get_info(self):                                 #метод класса 
#         info = {
#             'name': self.name,
#             "age": self.age,
#             "animal_type": self.animal_type
#         }
#         return info
#     def getget_info_arms(self):
#         return f'{self.arms} лапы у {self.animal_type}'




# dog = Animal('Bobik', 10, 'Sobaka')                      # экземпляр класса
# cat = Animal(name='Мурка', age=5, animal_type='kowka')       

# print(dog.get_info())
# # dog.name
# print(cat.name)
# print(dog.getget_info_arms())





# from winreg import REG_QWORD


# class Built():
#     def __init__(self, type_):
#         print('Я инициализируюсь!!!1')
#         self.check_type(type_=type_)
#         self.type_ = type_
    
#     def check_type(self, type_) -> None:
#         if not type_ in ['room', 'table']:
#             raise ValueError('я могу строить только комнаты и столы')

#     def __del__(self):
#         print(f'Удалился обьект как {self.type_}')

# room1 = Built(type_= 'room')

# del room1








# class Cart:
#     def __init__(self,title,status) -> None:
#         self.title = title
#         self.total = 0
#         self.status = status
#         self.history_pay = list()


#     def add_money(self, money):
#         self.total += money


#     def get_info_cart(self):
#         info = {
#             'Название карты': self.title,
#             'статус карты': self.status,
#             'общая сумма': self.total
#         }
#         return info
#     def payment(self, title, price):
#         if price > self.total:
#             print("недостаточно средств на карте")
#         else:
#             self.total -= price
#             print(f'успешная транзакция покупки {title} по цене {price}')
#             info = {'title': title, 'price': price}
#             self.history_pay.append(info)
    
#     def history(self):
#         return self.history_pay


# cart1 = Cart(title='VisaCart', status='normal')
# cart2 = Cart(title='elcart', status='vip')

# # print(cart1.total)
# cart1.add_money(45)
# # print(cart1.total)
# cart2.add_money(10000)
# # print(cart2.total)
# # print(cart1.get_info_cart())
# # print(cart2.get_info_cart())
# # cart1.text ='text'


# cart1.add_money(money=200000)
# cart1.payment(title='Шорты', price=500)
# cart1.payment(title='Lx600', price = 130000)
# print(cart1.get_info_cart())
# print(cart1.history())


# greeting = 'a'

#     type(greeting)







# class Song:
#     def __init__(self,title,author,year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def show_title(self):
#         print(f'Название этой песни {self.title}')
    
#     def show_author(self):
#         print(f'Автор этой песни {self.author}')
    
#     def show_year(self):
#         print(f'Эта песня вышла в {self.year} году')





# song = Song('Happy', 'Pharrell Williams', 2013)
# song.show_title()
# song.show_author()
# song.show_year()










# from curses.textpad import rectangle


# class Circle:
#     color = 'Синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return self.pi * self.radius ** 2     #task 2 
    
    
# circle = Circle(2)
# circle.color = 'Красный'
# circle.get_area()
# str






# class BankAccount:

#     def __init__(self):
#         self.balance = 0

#     def withdraw(self,amount):
#         self.balance -= amount
#         print(f'Ваш баланс: {self.balance} сом')              task 3

#     def deposit(self,amount):
#         self.balance += amount
#         print(f'Ваш баланс: {self.balance} сом')

# account = BankAccount()
# account.deposit(1000)
# account.withdraw(500)






# class Taxi:
#     def __init__(self, name, cost, cost_km):
#         self.name = name
#         self.cost = cost
#         self.cost_km = cost_km
#     def get_total_cost(self,km):
#         return f'Такси {self.name}, стоимость поездки: {self.cost + self.cost_km * km} сом'     task 4
# taxi1 = Taxi("Namba", 50, 10)
# taxi2 = Taxi('Yandex', 20, 10)
# taxi3 = Taxi('Jorgo', 30, 15)

# print(taxi1.get_total_cost(10)) 
# print(taxi2.get_total_cost(6)) 
# print(taxi3.get_total_cost(14))









# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone
    
#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')    task 5

# contact = Phone('John', 'Snow', +996707707707)
# contact.get_info()








# from datetime import datetime
# class Nobel:
#     def __init__(self, object, year, name):
#         self.category = object
#         self.year = year
#         self.winner = name

#     def get_year(self):
#         year = datetime.now().year - self.year
#         return f"выиграл {year} лет назад"


# winner1 = Nobel("Литература", 1971, "Пабло Неруда")
# print(winner1.category, winner1.year, winner1.winner)               TASk 7
# print(winner1.get_year())


# winner2 = Nobel("Литература", 1994, "Кэндзабуро Оэ")
# print(winner2.category, winner2.year, winner2.winner)
# print(winner2.get_year())






# class Math:
#     def __init__(self, value: int):
#         self.value = value
 
#     def get_factorial(self):
#         factorial = 1
#         for i in range(1,self.value+1):
#             factorial *= i
#         return factorial
    
#     def get_sum(self):
#         string = str(self.value)
#         summ = 0
#         for i in string:
#             summ += int(i)
#         return summ
    
#     def get_mul_table(self):
#         mul_table = ''
#         for i in range(1, 11):
#             mul_table += f'{self.value}x{i}={self.value * i}\n'             task 9 
#         return mul_table
    
# num = Math(11)
# print(num.get_factorial())
# print(num.get_sum())
# print(num.get_mul_table())






'''
  
                           НАСЛЕДОВАНИЕ ПРАКТИКА!!! 


'''
#СИНТАКСИС СОЗДАНИЕ родительских  и дочерних классов!
# class Parent:
#     pass

# class Child(Parent):
#     pass

# class A:
#     pass

# class B(A):
#     pass

# class C(B):
#     pass

#isinstance(obj, class)  проверяет является ли созданный обьект экземпляром класса  переданным в скобках вторым аргументомя
# a = A()
# b = B()
# c = C()
# print(isinstance(c, A))
# print(isinstance(c, B))
# print(isinstance(b, A))
# print(isinstance(a, B))






#НАСЛЕДОВАНИЕ МЕТОДОВ И АТРИБУТОВ В ДОЧЕРНИХ  КЛАССОВ

# from curses.textpad import rectangle


# class Polygon:
#     sides = 'many'
    
#     def __init__(self, *args, **kwargs):
#         self.args = args
#         self.kwargs = kwargs 
#         print(self.args)
#         print(self.kwargs)

#     def get_perimeter(self):
#         if self.args:
#             return sum(self.args)
#         elif self.kwargs:
#             return sum(self.kwargs.values())

# class Rectangle(Polygon):
#     sides = 4                             # (a + b) * 2
    
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def get_perimeter(self):
#         return (self.a + self.b) * 2


# class Triangle(Polygon):
#     sides = 3
    
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
    
#     def get_perimeter(self):
#         return self.a + self.b + self.c
    

# triangle1 = Triangle(a=2, b=3, c=4)
# print(triangle1.sides)
# print(triangle1.get_perimeter())




# rectangle = Rectangle(a=7, b=6)
# rectangle2 = Rectangle(a=9, b=2)
# print(rectangle.sides)
# print(rectangle.get_perimeter())
# print(rectangle.get_perimeter())
    
# polygon = Polygon(a=9, b=8, c=10, d=9, e=5)
# print(polygon.sides)
# print(polygon.get_perimeter())











#ФУНКЦИЯ super()










'''
|||||||||||||||||||||||||||||||||ЛЕКЦИЯ НАСЛЕДОВАНИЕ ООП!!!!!|||||||||||||||||||||||||

НАСЛЕДОВАНИЕ КЛАССОВ - это один из основных принципов ООП (полиморфизм, наследование, Инкапсуляция)
__method__ - it is magic method
'''

# class A:
#     pass                      
# print(A.__mro__)

# class A:

#     def __repr__(self):
#         return 'it is A class'
#     def __str__(self):
#         return 'A'
# # print(A.__repr__)
# a = A()
# print(a)


# from datetime import datetime 

# print(str(datetime.now()))
# print(repr(datetime.now()))



# class A():
#     name = 'it is A'

# class B(A):
#     pass
# print(B.__mro__)
# print(B.name)




# class People:             # родителский базовый класс
#     head = 'Голова'
#     arms = 'Руки'
    
# class UpdatePeople(People):                   # дочерний Класс
#     def __init__(self,name):
#         self.name = name

# people1 = People()
# print(people1.head)
# people2 = UpdatePeople('Nursultan')
# print(people2.arms, people2.name, sep='\n')





# class A:
#     pay = 1000

# class B(A):
#     money = 5000

# a = A()
# b = B()
# print(b.pay)
# print(a.money)



# class People:

#     head = 'голова'
#     arms = 'рука'
    
#     def __init__(self, fio, age,adress=None):
#         fio = People.split_fio(fio)
#         self.name = fio[1]
#         self.surname = fio[0]
#         self.last_name = fio[-1]
#         self.age = age
#         self.adress = adress
   

#     @classmethod
#     def split_fio(cls, fio):
#         return fio.split()

#     def __str__(self) -> str:
#         return self.name + ' ' + str(self.age) 
    

# class PeopleWithGender(People):
#     def __init__(self,fio, age, gender, adress=None):
#         fio = self.split_fio(fio)
#         self.age = age
#         self.gender = gender
#         self.adress = adress
#         self.name = fio[1]
#         self.surname = fio[0]
#         self.last_name = fio[-1]
    
#     def __str__(self) -> str:
#         return self.name + ' ' + self.gender

# class UpdatePeople(People):
#     def __init__(self, fio, age, genger, adress=None):
#         super().__init__(fio, age, adress)
#         self.gender = genger

#     def __str__(self) -> str:
#         return super().__str__() + ' ' + self.gender

    

# aigerim = PeopleWithGender('Testova Aigerim Tesrovna', 25, 'Female')
# Elina = People('Tetova elina Testovna', 22, adress='табышалиева 29')
# Dosbol = UpdatePeople('Dosbol Dosbolov Dosbolovich', 25, 'Male')
# print(Dosbol)

# # bots = (People(f'Bot Bot{i} Testova'))
# Erbol = People('Ажыбеков Эрбол Курманкулович', 100, adress = 'белинка 24')
# Isabar = People('Исабаров Исабар Исабарович', 25, adress = 'манаса 233')
# print(Elina)
# print(Erbol)
# print(Isabar)
# print(aigerim)




# class A:

#     def get_info(self):

#         return self.__class__
# class B(A):

#     def get_info(self):                    # переопределил метод  родительского  класса
#         return 'it is class BBBBB!!!!!'
#     name = 'name'

# class C(B):

#     def get_info(self):                       # 
#         return super().get_info() + 'test'


# a = A()
# b = B()
# c = C()
# print(a.name)
# print(b.get_info())
# print(a.get_info())
# print(a.__class__) # -> return class '__main__.A'>
# print(c.get_info())
# print(С.__mro__)




# class Newlist(list):
#     def __str__(self) -> str:
#         return ' '.join(map(lambda i: str(i),self))

# new_list = Newlist([1,2,3])
# print(new_list)





'''
АБСТРАКЦИЯ - это один из принципов ООП где есть абстрактное описание класса 
и от нее  не создаются  объекты(экземпляры)

'''

# from abc import ABC, abstractclassmethod

# class AbstractCart(ABC):

#     @abstractclassmethod
#     def __init__(self, title, status):

#         pass

#     @abstractclassmethod
#     def __str__(self) -> str:
#         pass
# class Cart(AbstractCart):
#     def __init__(self, title, status):
#         self.title = title
#         self.status = status

# class DemirCart(AbstractCart):
#     def __init__(self, title, status):
#         self.title = title
#         self.status = status

#     def __str__(self) -> str:
#         return self.title

# aitemir = DemirCart('VisaCart', status='normal')
# test = AbstractCart('test', 'test1')




# class Salary:
#     percent = 8
#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         return self.salary * self.percent / 100 * self.experience

# obj = Salary(10000, 10)
# print(obj.count_percent())








# class Sniper:

#   def init(self, name):
#     self.name = name
#     self.health = 100

#   def shoot(self, sniper):
#     sniper.health -= 20

# ag = Sniper('Kapitan Panika')
# pogchamp = Sniper('Magister Yoda')

# choices = (ag, pogchamp)
# while True:
#   shooter = random.choice(choices)
#   if shooter == ag:
#     shot = pogchamp
#   else:
#     shot = ag

#   shooter.shoot(shot)
#   print(f'Shooter {shooter.name} is shooting, {shot.name} has {shot.health} healts points.')     classs work 

#   if ag.health == 0:
#     print(f'{ag.name} is dead. {pogchamp.name} won')
#     break
#   elif pogchamp.health == 0:
#     print(f'{pogchamp.name} is dead. {ag.name} won')
#     break
#   else:
#     continue













# ... class Hogwarts:
#   faculties = {
#     'courage': 'Gryffindor',
#     'intelligence': 'Ravenclaw', 
#     'justice': 'Hufflepuff',
#     'ambition': 'Slytherin'
#   }

#   def init(self, courage, intelligence, justice, ambition):
#     self.courage = courage
#     self.intelligence = intelligence
#     self.justice = justice
#     self.ambition = ambition

#   def sorting_hat(self):
#     if self.courage > self.intelligence and self.justice and self.ambition:
#       print('Преобладает courage -> Gryffindor')
#     elif self.intelligence > self.courage and self.justice and self.ambition:
#       print('Преобладает intelligence -> Ravenclaw')
#     elif self.justice > self.intelligence and self.courage and self.ambition:
#       print('Преобладает justice -> Hufflepuff')
#     elif self.ambition > self.intelligence and self.justice and self.courage:
#       print('Преобладает ambition -> Slytherin')

# harry = Hogwarts(24, 20, 31, 10)
# peter = Hogwarts(21, 27, 37, 8)
# harry.sorting_hat()
# peter.sorting_hat()



# class Hogwarts:
#     faculties = {
#         'courage': 'Gryffindor',
#         'intelligence': 'Ravenclaw', 
#         'justice': 'Hufflepuff',
#         'ambition': 'Slytherin'
#     }

#     def __init__(self, courage, intelligence, justice, ambition):
#         self.courage = courage
#         self.intelligence = intelligence
#         self.justice = justice
#         self.ambition = ambition

#     def sorting_hat(self):
#         if self.courage > self.intelligence and self.justice and self.ambition:
#             print('Преобладает courage -> Gryffindor')
#         elif self.intelligence > self.courage and self.justice and self.ambition:
#             print('Преобладает intelligence -> Ravenclaw')
#         elif self.justice > self.intelligence and self.courage and self.ambition:
#             print('Преобладает justice -> Hufflepuff')
#         elif self.ambition > self.intelligence and self.justice and self.courage:
#             print('Преобладает ambition -> Slytherin')

# harry = Hogwarts(24, 20, 31, 10)
# peter = Hogwarts(21, 27, 37, 8)
# harry.sorting_hat()
# peter.sorting_hat()





# class Class1: 
#     def first(self):       task 1
#         pass
#     def second(self):
#         pass
    
# class Class2(Class1):
#     def third(self):
#         pass
#     def fourth(self):
#         pass

# obj = Class2()
# obj.first()
# obj.second()
# obj.third()
# obj.fourth()




# class My_list(list):
#     def __init__(self, inde, element):
#         self.inde = inde
#         self.element = element
    










# TASK CLASSWORK 1
# import random

# class Languages:
#     students_count = 0
#     def __init__(self):
#         Languages.students_count += 1
    
#     def coding(self):
#         raise NotImplementedError

# class Python(Languages):
#     students_count = 0

#     def __init__(self):
#         super().__init__()
#         Python.students_count += 1

#     def __str__(self):
#         return 'Python'
    
#     def coding(self):
#         print('I am Python student. I am coding now')

# class JavaScript(Languages):
#     students_count = 0

#     def __init__(self):
#         super().__init__()
#         JavaScript.students_count += 1


#     def __str__(self):
#         return 'JavaScript'

#     def coding(self):
#         print('I am JavaScript student. I am coding now')

# student1 = Python()
# student2 = JavaScript()


# my_choice = input('Guess the student"s languege\n')
# programm_choice = random.choice([student1, student2])

# programm_choice.coding

# if programm_choice.__str__() == my_choice:
#     print('Good job!!!')

# else:
#     print("No bueno:/ ")





# class Mylist(list):
#     def insert(self, arg1, arg2):
#         print('first arg - element, second arg - index')    task 2 classwork
#         return super().insert(arg2, arg1)

# list1 = Mylist([1, 2, 3, 4, 5])
# list1.insert('makers', 0)

# list2 = list([1, 2, 3, 4, 5])
# list2.insert(3, 'dafsdfs')

# print(list1)






# def is_admin(check):
#     if check == get_user[0]:
#         print('Доступ разрешен john133')
#     else:
#         print('Доступ запрещен john133')

# @is_admin
# def get_user(dict):
#     return dict
 
# get_user({'username': 'john133', 'is_admin': True})
# get_user({'username': 'jane133', 'is_admin': False})








# class MyDict(dict):
#     def get(self, key, default='Are you kidding?'): 
#         return dict.get(self, key, default)

# obj_dict = MyDict({'some_title': 2}) 
# print(obj_dict.get('some')) 







# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def display(self):
#         print(f'name:{self.name}, age:{self.age}')

# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty
  

#     def display_student(self):
#         super().display()
#         print(f'faculty:{self.faculty}')

# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# obj_student.display_student() 






# class Parent():
#     x = 1
#     y = 2

# class Child(Parent):
#     x = 111
#     y = 222

#     def mix(self):
#         return Parent.y

# c = Child()
# print(c.mix())

# a  = 'erbosha'
# b = [1,2,3,4,5]
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}
# print(len(a,b,c))









# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')

# rex = Dog()
# barsik = Cat()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik) 
# to_pet(rex)












# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print (f'name:{self.name}, age:{self.age}')


# class Student(Person):

#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print (f'name:{self.name}, age:{self.age}, faculty:{self.faculty}')


# obj_student = Student('Rick', 21, 'science')
# obj_student.display() 
# obj_student.display_student()






# class Anagram(str):

#     def eq(self, o: str) -> bool:
#         return sorted(self) == sorted(o)

#     def __mul(self, number):
#         return self[::-1] * number 

# word1 = Anagram('hello')
# word2 = Anagram('olleh')
# print(word1 == word2)
# print(word1 * 3)








class Student:

    def __init__(self, name, class_name, ball: dict):
        self.name = name
        self.class_name = class_name
        self.ball = ball

    def __gt__(self, other: object) -> str:
        return f"> {sum(self.ball.values()) > sum(other.ball.values())}"

    def __lt__(self, other: object) -> str:
        return f"< {sum(self.ball.values()) < sum(other.ball.values())}"

    def __ge__(self, other: object) -> str:
        return f">= {sum(self.ball.values()) >= sum(other.ball.values())}"

    def __le__(self, other: object) -> str:
        return f"<= {sum(self.ball.values()) <= sum(other.ball.values())}"

obj_student1 = Student('a', 'A', {'math': 100, 'history': 50, 'literature': 88})  
obj_student2 = Student('b', 'Aa', {'math': 100, 'history': 50, 'literature': 88})  
print(obj_student1 > obj_student2)  
print(obj_student1 < obj_student2)  
print(obj_student1 >= obj_student2)  
print(obj_student1 <= obj_student2)