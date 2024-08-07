import instaloader
from dotenv import load_dotenv
import os

load_dotenv()

def scrape_instagram_profile(username, password, profile_name, limit, target_type='followers', min_followers=0):
    loader = instaloader.Instaloader()
    help_me = "-=" * 25 + "-"

    try:
        print(f"Вход как {username}")
        loader.login(username, password)
        print("Вход успешен")

        print(f"Попытка загрузки профиля: {profile_name}")
        profile = instaloader.Profile.from_username(loader.context, profile_name)
        print(f"Профиль '{profile_name}' успешно загружен")

        if profile.is_private:
            print(f"Профиль {profile_name} закрыт. Парсинг невозможен.")
            return

        if target_type == 'followers':
            print('Получение подписчиков...')
            target_list = profile.get_followers()
        elif target_type == 'followees':
            print('Получение подписок...')
            target_list = profile.get_followees()
        else:
            print("Ошибка: Неверный тип цели. Введите 'followers' для подписчиков или 'followees' для подписок.")
            return

        print(f"Парсинг данных для профиля {profile_name} ({'подписчики' if target_type == 'followers' else 'подписки'})...")
        print(help_me)

        if limit:
            target_list = list(target_list)[:limit]
        
        for person in target_list:
            print(f"Обработка пользователя: {person.username}")
            print(help_me)
            if person.followers >= min_followers:
                user_info = {
                    "Логин": person.username,
                    "ID": person.userid,
                    "Количество подписчиков": person.followers,
                    "Количество контента": person.mediacount,
                }

                for key, value in user_info.items():
                    print(f"{key}: {value}")
                print(help_me)

    except Exception as e:
        print(f"Произошла ошибка: {str(e)}")


# Задайте переменные здесь
username = os.getenv("INSTAGRAM_USERNAME") # .env, ваш логин в Instagram
password = os.getenv("INSTAGRAM_PASSWORD") # .env, ваш пароль в Instagram
profile_name = "username" # Замените на нужное имя профиля для поиска
target_type = "followers" # "followers" для подписчиков, "followees" для подписок
min_followers = 0 # Минимальное количество подписчиков для фильтрации
limit = None # Лимит парсинга пользователей (int)

scrape_instagram_profile(username, password, profile_name, limit, target_type, min_followers)
