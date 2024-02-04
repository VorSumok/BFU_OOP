from abc import ABC, abstractmethod
import ast

class IUserManager(ABC):  # задает интерфейс для управления пользователями
    @abstractmethod
    def SignIn(self, user):
        pass

    @abstractmethod
    def SignOut(self, user):
        pass

    @abstractmethod
    def isAuthorized(self):
        pass


class IRepository(ABC):  # Этот класс задает интерфейс для работы с хранилищем данных
    @abstractmethod
    def GetAll(self):
        pass

    @abstractmethod
    def Add(self, item):
        pass

    @abstractmethod
    def Remove(self, item):
        pass

    @abstractmethod
    def Update(self, item):
        pass



class IUserRepository(IRepository): #интерфейс для получения пользователя по id и login
    @abstractmethod
    def GetById(self, id):
        pass

    @abstractmethod
    def GetByLogin(self, login):
        pass


class User: # представляет пользователя
    def __init__(self, id, login, password, name):
        self.id = id
        self.login = login
        self.password = password
        self.name = name

class FileUserRepository(IUserRepository):  #Этот класс предназначен для работы с файловым хранилищем пользователей

    def __init__(self, file_name):
        self.file_name = file_name

    def GetAll(self):
        try:
            with open(self.file_name, 'r') as file:
                users = file.readlines()
            users = [ast.literal_eval(user) for user in users]
        except FileNotFoundError:
            users = []
        return users

    def Add(self, user):
        with open(self.file_name, 'a') as file:
            file.write(str(user.__dict__) + '\n')

    def Remove(self, user):
        users = self.GetAll()
        users = [u for u in users if u['id'] != user.id]
        with open(self.file_name, 'w') as file:  #
            for user in users:
                file.write(str(user) + '\n')

    def Update(self, user):
        users = self.GetAll()
        for i, u in enumerate(users):
            if u['id'] == user.id:
                users[i] = user.__dict__
                break
        with open(self.file_name, 'w') as file:
            for user in users:
                file.write(str(user) + '\n')

    def GetById(self, id):
        users = self.GetAll()
        for user in users:
            if user['id'] == id:
                return User(**user)
        return False

    def GetByLogin(self, login):
        users = self.GetAll()
        for user in users:
            if user['login'] == login:
                return User(**user)

class FileUserLog(IRepository): #класс для работы с логами
    def __init__(self, file_log_name):
        self.file_log_name = file_log_name

    def Add(self, userID):
        with open(self.file_log_name, 'a') as file_log:  # Открываем файл в режиме добавления
            file_log.write(str(userID) + '\n')  # Записываем словарь пользователя в новую строку

    def GetLastEntry(self):
        last_user_id = 0
        try:
            with open(self.file_log_name, 'r') as file_log:
                copy_log = file_log.readlines()
                if len(copy_log) != 0:
                    last_user_id = int(copy_log[-1])
        except FileNotFoundError:
            print("Не удалось открыть файл с логами")
        return last_user_id

    def GetAll(self):
        try:
            with open(self.file_log_name, 'r') as file_log:
                copy_log = file_log.readlines()
        except FileNotFoundError:
            print("Не удалось открыть файл с логами")
            copy_log = []
        return copy_log

    def Update(self, item):
        raise AttributeError("'FileUserLog' object has no attribute 'Update'")

    def Remove(self, item):
        raise AttributeError("'FileUserLog' object has no attribute 'Remove'")
class AuthManager(IUserManager):
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.current_user = None

    def SignIn(self, user):
        self.current_user = user

    def SignOut(self, user):
        self.current_user = None

    def isAuthorized(self):
        return self.current_user is not None


def main_menu():
    print("1. Регистрация нового пользователя")
    print("2. Авторизация")
    print("3. Завершить работу")
def user_menu():
    print("1. Сменить пользователя")
    print("2. Завершить работу")
    while True:
        user_choice = input("Выберите действие: ")
        if user_choice == "1":
            # Логика для смены пользователя
            if auth_manager.isAuthorized():
                print(f"Текущий пользователь {auth_manager.current_user.name} вышел из системы.")
                user_log.Add(-auth_manager.current_user.id)
                auth_manager.SignOut(auth_manager.current_user)
                break
        elif user_choice == "2":
            exit()
        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий вариант.")



if __name__ == '__main__':


    user_repository = FileUserRepository("users.json")
    user_log = FileUserLog("user.log")
    auth_manager = AuthManager(user_repository)
    # Логика для автоавторизации последнего вошедшего пользователя
    last_user = user_repository.GetById(user_log.GetLastEntry())
    if last_user:
        auth_manager.SignIn(last_user)
        print(f"Вы автоматически авторизовались за последнего пользователя {last_user.name}.")
        user_menu()
    else:
        print("Никто не авторизован.")


    while True:
        main_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            # Логика для регистрации нового пользователя
            id = len(user_repository.GetAll()) + 1  # Автоматическое назначение ID
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            name = input("Введите имя: ")
            new_user = User(id, login, password, name)
            user_repository.Add(new_user)

        elif choice == "2":
            # Логика для авторизации
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            user = user_repository.GetByLogin(login)
            if user and user.password == password:
                auth_manager.SignIn(user)
                user_log.Add(user.id)
                print(f"Вы успешно авторизовались как {user.name}.")
                user_menu()
            else:
                print("Неверный логин или пароль.")
        elif choice == "3":
            break
        else:
            print("Некорректный выбор. Пожалуйста, выберите существующий вариант.")