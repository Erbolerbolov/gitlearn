# # class Parent:
# #     def who_am_i(self):
# #         print('i am a perent')



# # class Child(Parent):
# #     def who_am_i(self):
# #         super().who_am_i()
# #         print('i am a child')


# # child = Child()
# # child.who_am_i()



# # class Grandpa:
# #     def talant(self):
# #         print('i am good dancing')

# # class Grandma:
# #     def talant(self):
# #         print('i am good singing')

# # class Father:
# #     last_name = 'White'

# #     def talant(self):
# #         print('i can build houses')


# # class Mother(Grandpa, Grandma):
# #     last_name = 'Brown'

# #     def talant(self):
# #         print('i am good at cooking')

# # class Child(Father, Mother):
# #     pass

# # child = Child()
# # # print(child.last_name)
# # # child.talant()
# # print(Child.mro())









# # class A:
# #     def __init__(self, param):
# #         print(f'Hey, i"s A class, i got {param}parameters')

# #     def get_letter(self):
# #         print('aaaaa')

# # class B:
# #     def __innit__(self, param):
# #         print(f'Hey, i,s B class, I got {param} parameters')

# #     def get_letter(self):
# #         print('bbbb')

# # class C(A,B):
# #     def get_letter(self):
# #         print('cccc')
    
# # c = C('Makers')
# # c.get_letter()
# # print(C.mro())
# # c.get_letter()
# # c.get_letter()





# #!!!!!!!!!!#Diamond Problem.!!!!!!!!!!



# # class A:

# #     def method(self):
# #         print('hello iam A')

# # class B(A):
# #     def method(self):
# #         super().method()
# #         print('hello iam B')

# # class C(A):
# #     def method(self):
# #         super().method()
# #         print('hello iam C')

# # class D(B,C):
# #     pass
# #     # def method(self):
# #     #     print('Hey ,D')


# # d = D()
# # d.method()
# # print(D.mro())
         




# # МИКСИНЫ
# # SOLID

# # class Bird:
# #     def __init__(self):
# #         print('i am a bird')

# # class FlyMixin:
# #     def fly(self):
# #         print(' i can fly')
    

# # class Hawk(Bird, FlyMixin):
# #     pass

# # class Eagle(Bird, FlyMixin):
# #     pass

# # class Pinguin(Bird):
# #     pass


# # hawk = Hawk()
# # hawk.fly()

# # eagle = Eagle()

# # ping = Pinguin()











# """

# !!!!!!!MRO: Method Resolution Order!!!!

# порядок решений методов 
# порядок обхода по иерархии наследования

# """

# '''

# Множественное наследование  принцип ООП который заключается в возможности дочернего класса наследовать функционал и атрибуты не от одного, а от нескольких родителей 

# '''



# # class A:
# #     wheel = 4
# #     def method1(self):
# #         print('this is class A')

# # class B:
# #     def method2(self):
# #         print('this is class B')

# # class C(A,B):
# #     def method3(self):
# #         print('this is class C')


# # c = C()
# # c.method1()
# # c.method2()
# # c.method3()
# # print(c.wheel)



# # class Auto:
# #     def ride(self):
# #         print('riding on grond')

# # class Boat:
# #     def swim(self):
# #         print("floating on water")

# # class Amphibian(Auto, Boat):
# #     pass

# # obj = Amphibian()
# # obj.ride()
# # obj.swim()

# # print(isinstance(obj, Auto))
# # print(isinstance(obj, Boat))
# # print(isinstance(obj, Amphibian))









# ''''
# Mixins - Классы примеси
# 1.  от них не следует создавать обьекты (так как они не являются расширителями функционала других классов, и не считаются полноценными классами)

# '''


# # class RadioMixin:
# #     def play_music(self):
# #         print('play some music')

# # class Auto:
# #     pass

# # class Boat:
# #     pass

# # class AutoWithRadio(Auto, RadioMixin):
# #     pass

# # obj = AutoWithRadio()
# # obj.play_music()





# # class Agile:
# #     def create(self):
# #         print('forming class agile')

# # class Dev(Agile):
# #     def create(self):
# #         print('Forming class Dev')

# # class QA(Agile):
# #     def create(self):
# #         print('forming class QA')
    
# # class Sprint(Dev, QA):
# #     pass

# # sprint = Sprint()
# # sprint.create()
# # print(Sprint.mro())
# # print(Sprint.__mro__)






# # class A:
# #     def method1(self):
# #         return 'A'

# # class B(A):
# #     def method1(self):
# #         return 'B'

# # class C(A):
# #     pass
# #     # def method1(self):
# #     #     return 'C'

# # class D(C):
# #     def method1(self):
# #         return 'D'

# # class E(C):
# #     pass
# #     # def method1(self):
# #     #     return 'E'

# # class F(B, E):
# #     pass
# #     # def method1(self):
# #     #     return 'F'

# # f = F()
# # print(f.method1())
# # # print(F.mro)


# class A:

#     def test(self):
#         print('Class A')


# class B(A):
#     def test(self):
#         print('class B')


# class C(A):
#     pass

# class D(B,C):
#     pass


# c = D()
# c.test()







# наследование с перезаписыванием!



# from tkinter import NE


# class Base:
#     def base_func(self):
#         print('Method of Base class')

# class Child(Base):
#     def base_func(self):
#         print('Method of class Child')
#         # return super().base_func()
    
# class NextChild(Child):
#     def base_func(self):
#         print('Method of class NextChild')
#         # return super().base_func()


# obj = NextChild()
# obj.base_func()




# class TeamMember:


#     def __init__(self, name, *args, **kwargs):
#         self.name = name
#         # print('args', args)
#         # print('kwargs', kwargs)
#         self.last_name = kwargs['last_name']
    
#     def get_info(self):
#         return f'{self.name} {self.last_name}'


# obj = TeamMember('test1', 1, 2, 3, 4, last_name = 'test12312423fsd')
# print(obj.get_info())





# from urllib import response
# import requests
# from bs4 import BeautifulSoup as bs
# from env import config

# URL = config['URL']


# class ParserKivano: 
#     def __init__(self, url: str, category: str, page):
#         self.url = url
#         self.category = category
#         self.page = page

    
#     def get_full_url(self, page):
#         return self.url + self.category + '?page=' + str(page)
    
#     def get_response(self, page):
#         response = requests.get(self.get_full_url(page))
#         return response.text

#     def get_soup(self, page):
#         html = self.get_response(page)
#         soup = bs(html, 'lxml')
#         return soup

#     def get_data_list(self):
#             for _ in range(1, self.page+1):
#                 print(f'we parsing {_} page')

#                 soup = self.get_soup(_)
#                 all_list = soup.find('div', class_='list-view').find_all('div', class_='item')
#                 for product in all_list:
#                     product: bs
#                     right = product.find('div', class_='pull-right')
#                     try:
#                         title = right.find('div', class_='product_text').find('strong').text
#                     except:
#                         title = '-'
#                     else:
#                         print(title)
        

# obj = ParserKivano(URL, 'elektronika', 20)
# # obj.get_data_list()
# obj1 = ParserKivano(URL, 'detskie-tovary', 3)
# obj1.get_data_list()
    






