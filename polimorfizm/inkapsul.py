'''

Модификаторы доступа Python

'''


'''
Модификаторы доступа:
1. PUBLIC(публтчный) - password, get_info() писать как обычно без нижних подчеркиваний
2. protected(защищенный) - _password, _get_info() защищеным делает! писать через одно подчеркивание
3. private(скрытый) __password, __get_info() делает приватным! писать через два подчеркивания!


'''


# class User:
#     def __init__(self, username, password):
#         self.username = username
#         self.__password = password

#     def get_password(self, username):
#         if self.username == username:
#             return self.__password
#         else:
#             return 'NO!!!'
    
#     def set_password(self, old_password, new_password):
#         if self.__password == old_password:
#             self.__password = new_password
#         else:
#             return 'NO'

    
#     def __get_info(self):
#         print(f'Username {self.username}, password {self.__password}')


# user1 = User(username = 'makers123', password = 'bootcamp567')
# print(user1.username)
# print(user1.get_password(username='makers123'))
# user1.set_password(old_password='bootcamp567',
#        new_password='Helloworld777')
# print(user1.get_password(username='qwerty'))
# print(user1.get_password(username='makers123'))






# class Divider:
#     def __init__(self):
#         self.__divide_num = 1


#     @property               # -> getter v roli
#     def divider(self):
#         return self.__divide_num


#     @divider.setter             # -> setter v roli
#     def set_divider(self, value):
#         if not value == 0:
#             self.__divide_num = value
#             return 'successfully change divide number'
#         else:
#             return 'NO'

#     def divide(self, value):
#         return value / self.__divide_num

# obj = Divider()
# print(obj.divider)
# print(obj.divide(7))
# obj.divider = 14
# print(obj.divider)







# class Person:
    
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
#     @property
#     def full_name(self):
#         return f'{self.name}, {self.last_name}'

# person = Person(name='John', last_name='Snow')
# print(person.full_name())

# person = Person()
# person.name = 'Makers'
# person.age = 2
# print(person.name)
# print(person.age)

    




# class Car:

#     def _inject_fuel(self):
#         print('inject feuel')

#     def _init_bang(self):
#         print('Bang!!!!')


#     def _send_signal_to_ignition_system(self):
#         print('Ignition started')
#         self.inject_fuel()
#         self._init_bang()


#     def _send_signal_to_pc(self):
#         print('start')
#         self._send_signal_to_ignition_system()
    

#     def start_engine(self):
#         self._send_signal_to_pc()

# car = Car()
# car.start_engine()
# # car._init_bang()










'''
отличия 
1. underscore

2. protected - мы еще можем получить скрытые данные 

3.protected данные  наследуются в дочерних классах 
'''

# class A:
#     def _say_hello(self):
#         print('hello, makers')

# class B(A):
#     pass

# b = B()
# b.__say_hello()



# class A:

#     def method1(self):
#      print('Hello World')

# class B(A):
#     pass



# b1 = B()
# b1.method1()

'''

Инкапсуляция - это защита(сокрытия) данных от внешнего воздействия



'''



# class Person:
#     ID = 0  # атрибут класса ПУБЛИЧНЫЙ

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         # self.id = Person.ID
    
#     def get_info(self):
#         return f'name:{self.name} , age: {self.age}'

# Aitemir = Person('Aitenir', 25)
# Person.ID = 55
# print(Aitemir.ID)
# elina = Person('Elina', 23)
# print(elina.id)






# class Person:
#     _ID = 0 # ЗАщищеный protected

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.id = Person._ID
#         Person._ID += 1


# Person._ID = 55
# Edige = Person('Edige', 25)
# Almaz = Person('Almaz', 20)
# test = Person('Almaz', 20)
# print(Edige._ID)
# print(Almaz.id)
# print(test.id)



# class User:
#     __ID = 0
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         self.id = User.__ID
#         User.__ID += 1

# Almaz = User('Almaz', 'Almz@gmail.com')
# aktan = User("Aktan", 'Aktan@mail.ru')
# for id_ in (Almaz, aktan):
#     print(id_.__ID)
# print(dir(Almaz))


# from utils import check_email

# class TwitterUser:

#     def __init__(self, name, email) -> None:
#         self.name = name
#         self.__email = email
    
#     def get_email(self):
#         return self.__email


#     @check_email
#     def set_email(self, new_email):
#         self.__email = new_email
    

# User1 = TwitterUser('Daria', 'DaRia@gmail.com')
# print(User1.get_email())
# User1.set_email('Daria@mail.com')
# print(User1.get_email())



# from this import d


# class TelegramCreateUser:
#     __ID = 0
    
#     def __init__(self, phone, password, name = None, username = None):

#         self.__phone = phone
#         self.__password = password
#         self.name = name if not name is None else 'AnonymUser'
#         self.username = username
#         self.id = self.get_id()
#         self.increment_id()

#     def get_id(self):
#         return self.__ID

#     @classmethod
#     def increment_id(cls):
#         cls.__ID += 1


#     @property
#     def get_password(self):
#         return self.__password

#     @password.setter
#     def set_password(self, new_password):
#         self.__password = new_password
    
#     # password = property(get_password, set_password)



# user = TelegramCreateUser('+996709809090', '12345678', 'Azim', '@AzimKG')
# user2 = TelegramCreateUser('+996709909090', '12345678', 'Muha', '@MuhaKG')
# print(user.id, user2.id, sep='\n')
# user.password = 5555
# print(user.password)



# from accessify import private

# class A:

#     _a = 5     #protect
#     __b = 55    # private

#     @private
#     def __get_b(self):
#         return self.__b

# class B(A):

#     pass

# b = B()
# print(dir(b))
# # print(b._a)   #protected
# # print(b._A__b)
# # print(b._A__b)
# print(b._A__get_b())


# class BaseUser:
#     def get_info(self):
#         return f'{self.name} {self.email}'

# class User(BaseUser):
    
#     def __init__(self, name, email):

#         self.name = name 
#         self.__invalid_email(email=email)
#         self.email = email

#     def __invalid_email(self, email):
#         if not '@' in email:
#             raise ValueError('Ты дурак!!!')
    
#     def __str__(self) -> str:
#         return self.__class__.__name__

# user = User('user', 'bred@.com')
# # user.invalid_email('testgmail.com')
# print(user.get_info())
# print(user.name, user.email)








# class A:
#     def public(self):
#         return 'Public method'

    
#     def _protected(self):
#         return 'Protected method'


#     def __private(self):
#         return 'Private method'

# obj1 = A()
# print(obj1.public())
# print(obj1._protected())
# print(obj1._A__private())





# class Car:
#     def __init__(self):
#         self.__speed = 0

    
#     @property
#     def show_speed(self):
#         return self.__speed

#     @speed.setter
#     def set_speed(self, new):
#         self.__speed = new

# car1 = Car(0) 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)





# class Car:
#     def init(self):
#         self.__speed = 0
        
#     @property
#     def speed(self):
#         return self.__speed

#     @speed.setter
#     def speed(self, value):
#         self.__speed = value


# car1 = Car() 
# print(car1.speed) 
# car1.speed = 20 
# print(car1.speed)






#   taks 1 class work


# from datetime import datetime

# class Smartphone:
#     def call(self, phone_number):
#         print(f'Calling to {phone_number} number')

#     def where_to_wear(self):
#         print('you can keep me anywhere')



# class Watch:
#     def see_time(self):
#         print(f'its {datetime.now} now')
    
#     def where_to_wear(self):
#         print('You should wear me on yor hand')


# class SmartWatch(Watch, Smartphone):
#     pass



# smartwatch = SmartWatch()
# smartwatch.call(phone_number='900909090')
# smartwatch.see_time()
# smartwatch.where_to_wear()





# class CheckMixin:
#     def check(self, username , password):
#         if self.username == username and self.password == password:
#             print('successfully created')
#             self.count += 1
#         else:
#             print('Wrong credentials')


# class Instagram(CheckMixin):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.count = 0

#     def post_post(self, title, username, password):
#         super().check(username=username, password=password)
#         print(f'New post {title}')



# class Tiktok(CheckMixin):
#     def __init__(self, username, password):
#         self.username = username
#         self.password = password
#         self.count = 0
    
#     def post_video(self, video, username, password):
#         super().check(username=username, password=password)
#         print(f'new video {video}')

# obj1 =  Instagram(username='makers123', password='qwerty123')
# obj1.post_post(title='we are makers', username='makers123', 
#                 password='qwerty123')
# obj1.post_post(title='Test post', username='123makers',
#                 password='qwerty')

# print(obj1.count)

# obj2 = Tiktok(username='bootcamp678', password='asd678')
# obj2.post_video(video='we are bootcamp', username='bootcamp678', password='asd678')
# print(obj2.count)






from datetime import datetime

now = datetime.now()
class Clock:
    def current_time(self):
        print(now.strftime('%H:%M:%S'))

class Alarm:
    def on(self):
        print('Будильник включен')
    
    def off(self):
        print('Будильник выключен')

class AlarmClock(Clock,Alarm):
    def alarm_on(self):
        return super().on()

clock = AlarmClock()
clock.current_time() 
clock.alarm_on()
