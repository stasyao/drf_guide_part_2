# Учебный проект для пособия по Django Rest Framework

Статьи на Хабре:
+ [Django Rest Framework для начинающих: создаём API для записи и обновления данных (часть 1)](https://habr.com/ru/company/yandex_praktikum/blog/567564/)
+ [Django Rest Framework для начинающих: создаём API для записи и обновления данных (часть 2)](https://habr.com/ru/company/yandex_praktikum/blog/594141/)

Запускаем проект на своей машине: 

1. Клонируем репозиторий `git clone https://github.com/stasyao/drf_guide_part_2`
2. Переходим в папку с проектом `cd drf_guide_part_2` (здесь и далее приводятся команды в bash-терминале на машине под win)
3. Устанавливаем виртуальное окружение `python -m venv env`
4. Запускаем виртуальное окружение `source env/Scripts/activate`
5. Обновляем pip `python -m pip install --upgrade pip`
6. Устанавливаем в виртуальном окружении зависимости для проекта `python -m pip install --no-cache-dir -r requirements.txt`
7. Делаем миграции для создания базы данных `python manage.py migrate`
8. Заполняем базу данными &mdash; `python manage.py loaddata fixture.json`
9. Запускаем локальный сервер `python manage.py runserver`
10. По адресу `http://localhost:8000` будет доступен `Browsable API` (наглядное представление того, как работает API проекта).  
11. Чтобы управлять записями в БД через админку, создайте суперпользователя (`python manage.py createsuperuser`). Вход в админку `http://localhost:8000/admin`.  
