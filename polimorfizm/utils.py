def check_email(func):

    def wrapper(self,email):
        if type(email) != str:
            raise TypeError('Типовая ошибка')
        if not '@' in email:
            raise ValueError('Email invalid')
        func(self,email)

    return wrapper