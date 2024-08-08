# Instagram Scraper
Парсер для Instagram, с помощью которого, вы сможете узнать основную информацию об аккаунтах подписчиков или подписок какого либо пользователя.
## Технологии и пакеты
* Python
* Instaloader
* Python-dotenv
## Локальный запуск (Linux)
1. Перейдите в директорию проекта, затем создайте и активируйте виртуальное окружение
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. Установите зависимости
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

3. Создайте файл .env и установите необходимые ключи (INSTAGRAM_USERNAME, INSTAGRAM_PASSWORD)
   ```bash
   touch .env
   ```

4. В самом конце кода, в файле main.py установите значения необходимых переменных (profile_name, target_type, min_followers, limit)

5. Запустите скрипт
   ```bash
   python main.py
   ```
