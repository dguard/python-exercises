from time import sleep
import hashlib

class User:

    def __init__(self, nickname, password, age, salt):
        self.nickname = nickname
        self.password = password
        self.age = age
        self.salt = salt

    def __repr__(self):
        return self.nickname

class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode
        self.time_now = time_now

    def __repr__(self):
        return self.title

    def __str__(self):
        return self.title

class UrTube:

    def __init__(self, users=None, videos=None, current_user=None):
        if users is None:
            users = []
        self.users = users

        self.data = {}

        if videos is None:
            videos = []
        self.videos = videos

        self.current_user = current_user

    def log_in(self, nickname, password):
        if self.data.get(nickname):
            pass
        else:
            print("Пользователь не найден")
        salt = self.data[nickname].salt

        if self.data[nickname].password == hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest():
            self.current_user = self.data[nickname]
            print(f"Добро пожаловать, {self.current_user.nickname}")
        else:
            print("Неверный пароль")

    def register(self, nickname, password, password_repeat, age):
        if self.data.get(nickname):
            print(f'Пользователь {nickname} уже существует')
            return

        if password == password_repeat:
            pass
        else:
            print("Пароли не совпадают")

        import hashlib, uuid
        salt = uuid.uuid4().hex
        hashed_password = hashlib.sha512(password.encode('utf-8') + salt.encode('utf-8')).hexdigest()

        user = User(nickname, hashed_password, age, salt)
        self.users.append(user)
        self.data[nickname] = user

    def logout(self):
        self.current_user = None

    def add(self, *args):
        titles = set()
        for video in self.videos:
            titles.add(video.title)

        for video in args:
            if video.title in titles:
                pass
            else:
                self.videos.extend([video])
                titles.add(video.title)

    def get_videos(self, title):
        found = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                found.append(video)
        return found

    def watch_video(self, movie_name):
        if self.current_user:
            pass
        else:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if movie_name == video.title:
                if video.adult_mode and self.data[self.current_user.nickname].age >= 18:
                    pass
                elif video.adult_mode == False:
                    pass
                else:
                    print("Вам нет 18 лет, пожалуйста, покиньте страницу")
                    return
                for i in range(10):
                    sleep(1)
                    video.time_now += 1
                    print(f"{i+1}", end=" ")
                    if (i+1) == 10:
                        video.time_now = 0
                        print(" Конец видео")
                return
        # print("Видео не найдено")



if __name__ == '__main__':

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(str(ur.get_videos('лучший')))
    print(str(ur.get_videos('ПРОГ')))

    ur.watch_video('Для чего девушкам парень программист?')

    # while True:
    #     choice = int(input("Выберите действие: 1 - Вход, 2 - Регистрация "))
    #
    #     if choice == 2:
    #         print("Регистрация")
    #         ur.register(input("Введите ник: "), input("Введите пароль: "), input("Введите пароль еще раз: "), int(input("Введите возраст: ")))
    #
    #     if choice == 1:
    #         print("Вход")
    #         ur.log_in(input("Введите ник: "), input("Введите пароль: "))

    ur.register('vasya_pupkin', 'lolkekcheburek', 'lolkekcheburek', 13)
    ur.log_in('vasya_pupkin', 'lolkekcheburek')

    ur.watch_video('Для чего девушкам парень программист?')

    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 'iScX4vIJClb9YQavjAgF', 25)
    ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')