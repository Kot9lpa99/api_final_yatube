# API для Yatube
###### Апишка для соцсети Yatube. Через нее можно делать запросы к Постам, Группам, Коментам и Фоловерам. 
###### Возвращает данные в JSON.
***
#### Используемые технологии и библиотеки:
- [Python 3.7.0](https://www.python.org/doc/)
- [Django 2.2.16](https://docs.djangoproject.com/en/4.1/releases/2.2.16/)
- [Django REST framework 3.12.4](https://www.django-rest-framework.org/)
- [Simple JWT 4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
***
#### Для начала необходимо клонировать репозиторий:
```
git clone git@github.com:Kot9lpa99/api_final_yatube.git
```
##### Далее перейти в его папку:
```
cd api_final_yatube
```
##### Создаем виртуальное окружение:
```
python -m venv venv
```
##### Активируем на *nix-системах:
```
source venv/bin/activate
```
##### Активируем на Windows системах:
```
source venv/Scripts/activate
```
##### Устанавливаем зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
##### Выполняем миграции в папке с файлом manage.py:
```
python manage.py migrate
```
##### Запускаем проект:
```
python manage.py runserver
```
##### Проект доступен по адресу:
```
http://127.0.0.1:8000/api/v1/
```
##### Админка:
```
http://127.0.0.1:8000/admin
```
---
#### Примеры запросов:
###### Пример POST-запроса для аутентифицированного пользователя: добавление нового поста. POST 
```
http://127.0.0.1:8000/api/v1/posts/
```
###### пример запроса:
```
{
    "text": "Message To The World! HELLO WORLD!!"
}
```
###### Пример ответа:
```
{
    "id": 1,
    "author": "Kenny",
    "text": "Message To The World! HELLO WORLD!!",
    "pub_date": "2022-10-22T22:18:54.890979Z",
    "image": null,
    "group": null
}
```
###### Пример POST-запроса для авторизованного пользователя: отправляем новый комментарий к посту с id=1:
```
http://127.0.0.1:8000/api/v1/posts/1/comments/
```
```
{
    "text": "HELLOOOooO",
    "post": "1"
}
```
###### Пример ответа:
```
{
    "id": 1,
    "author": "Kenny",
    "text": "HELLOOOooO",
    "created": "2022-10-23T00:03:00.094704Z",
    "post": 1
}
```
#### Полный список возможных запросов к Апишке можно посмотреть вот по этому адресу:
```
http://127.0.0.1:8000/redoc/
```
#### Автор: 
##### Дубихин Егор
