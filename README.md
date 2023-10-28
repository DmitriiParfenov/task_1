# task_1

Task_1 — это решение тестового задания на позицию `Backend-разработчик (Python)` в компанию `ПИКАССОВ`.

# Дополнительная информация

- Для просмотра покрытия кода тестами введите в консоли:
```
coverage run --source='.' manage.py test
coverage report
```
- Для получения качественного анализа программного кода введите в консоли:
```
flake8 --config .flake8
```

- Для запуска отложенных задач выполните в консоли из директории `task_1`: </br>
```
celery -A config worker -l info
```

# Клонирование репозитория

В проекте для управления зависимостями используется [poetry](https://python-poetry.org/). </br>
Выполните в консоли: </br>

Для Windows: </br>
```
git clone git@github.com:DmitriiParfenov/task_1.git
python -m venv venv
venv\Scripts\activate
pip install poetry
poetry install
```

Для Linux: </br>
```
git clone git@github.com:DmitriiParfenov/task_1.git
python3 -m venv venv
source venv/bin/activate
curl -sSL https://install.python-poetry.org | python3
poetry install
```
# Установка и настройка Redis

- Установите Redis, если он не установлен. Для этого выполните в консоли:
```
sudo apt install redis-server
``` 
- Запустите Redis, выполнив в консоли:
```
sudo service redis-server start
``` 
- Произойдет запуск Redis сервера на порту 6379. Для того, чтобы убедиться, что сервер запущен, необходимо выполнить
в консоли команду, ответом которой должен быть `PONG`.
```
redis-cli ping
```

# Работа с базой данной PostgreSQL

- Установите PostgreSQL, если он не установлен. Для этого, например для Ubuntu, выполните в консоли:
```
sudo apt install postgresql
```
- Выполните вход в интерактивную оболочку PostgreSQL от имени `postgresql`, выполнив в консоли:
```
sudo -i -u postgres psql
```
- Создайте базу данный для проекта, выполнив в консоли:
```
CREATE DATABASE task_1;
```
- Закройте интерактивную оболочку PostgreSQL:
```
\q
```
# Работа с переменными окружения

- В директории `task_1` создайте файл `.env`. Пример содержимого файла:
- Пример содержимого файла `.env` для запуска сервиса через docker:
```
HOST=название текущего хоста — db (из docker-compose)
NAME=название базы данных — postgres
USER=имя текущего пользователя — postgres
PASSWORD=пароль текущего пользователя — ваш пароль

POSTGRES_USER=имя пользователя — postgres
POSTGRES_PASSWORD=пароль пользователя — ваш пароль 
POSTGRES_DB=название базы данных для подключения из docker — db (из docker-compose)

EMAIL_BACKEND=путь импорта Python для вашего класса бэкенда
EMAIL_HOST=хост SMTP
EMAIL_HOST_USER=адрес электронной почты для аутентификации на почтовом сервере
EMAIL_HOST_PASSWORD=пароль для аутентификации на почтовом сервере

LOCATION=местоположение используемого кеша (redis://redis:6379)
``` 
- Пример содержимого файла `.env` для запуска сервиса на локальной машине без docker:
```
HOST=название текущего хоста — localhost
NAME=название базы данных — task_1
USER=имя текущего пользователя — postgres
PASSWORD=пароль текущего пользователя — ваш пароль

POSTGRES_USER=имя пользователя — postgres
POSTGRES_PASSWORD=пароль пользователя — ваш пароль 
POSTGRES_DB=название базы данных для подключения из docker — db (из docker-compose)

EMAIL_BACKEND=путь импорта Python для вашего класса бэкенда
EMAIL_HOST=хост SMTP
EMAIL_HOST_USER=адрес электронной почты для аутентификации на почтовом сервере
EMAIL_HOST_PASSWORD=пароль для аутентификации на почтовом сервере

TELEGRAM_API_KEY=местоположение используемого кеша (redis://127.0.0.1:6379)
``` 

# Работа с миграциями

Из директории `task_1` выполните в консоли: </br>

```
python manage.py migrate
```

# Запуск сервера Django

- Активируйте виртуальное окружение согласно п. `Клонирование репозитория` </br>

- Из директории `task_1` выполните в консоли: </br>
```
python3 manage.py runserver
```
- Запустите отложенные задачи, выполнив в консоли: </br>
```
celery -A config worker -l info
```

# Запуск сервера Django c использованием docker-compose

- Установите `docker` согласно инструкции на сайте [docker](https://www.docker.com/get-started/). </br>
- Запустите образ для запуска нескольких контейнеров с использованием `docker-compose`. Для этого из директории `task_1` выполните в консоли: </br>
```
docker-compose build
```
- Запустите собранный образ. Для этого из директории `task_1` выполните в консоли: </br>
```
docker-compose up
```
- Или для запуска образа в фоновом режим из директории `task_1` выполните в консоли: </br>
```
docker-compose up -d
```
- Сервис будет доступен по URL `http://127.0.0.1:8000/` </br>
- Для остановки работы образа из директории `task_1` в консоли нажмите `CTRL + C`: </br>
- Для удаления остановленного образа из директории `task_1` в консоли выполните: </br>
```
docker-compose down
```
