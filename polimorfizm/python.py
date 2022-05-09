# from polimorphizm import Car, Ship, Airplane, Train

# person1 = Car('Honda')
# person3 = Car('Toyota')
# person2 = Ship('Titanic')
# person4 = Ship('SomeShip')
# person5 = Airplane('Erbosha')
# person6 = Train('Sometrain')



# for person in (person1, person2, person3, person4, person5, person6):
#     person.go('makers')
    



# from polimorphizm import Cat, Dog, Duck
# animal1 = Cat('tom', 6)
# animal2 = Dog('erb', 7)
# animal3 = Duck('habib', 29)
# animal4 = Cat('dafsd', 5)
# animal5 = Dog('Tuzik', 123)
# animal6 = Duck('ffsfs', 22)

# def func(animal):
#     animal.info()
#     animal.make_sound()

# func(animal1)
# func(animal2)
# func(animal3)
# func(animal4)
# func(animal5)
# func(animal6)
from error import PasswordError

def get_split_info(fio: str) -> list:
    '''
    Функция возвращает список из ФИО через пробел
    '''
    return fio.split()


def password_input_and_check():
    password = input('enter passwrod: ')
    pasword_confirm = input('enter pasword confirm: ')
    if len(password) < 8:
        raise PasswordError('Пароль слишком короткий')
    if password != pasword_confirm:
        raise PasswordError('Пароли не совпадают!!')
    return password
    
