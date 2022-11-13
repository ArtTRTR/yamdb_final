# yamdb_final
yamdb_final
![yamdb final deploy](https://github.com/ArtTRTR/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg?branch=master)

# **YaMDb Project**

### _СI и CD проекта API YaMDb_

# Описание

Проект **YaMDb** собирает **отзывы (Review)** пользователей на **произведения (Titles)**. Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список **категорий (Category)**.

Сами произведения в **YaMDb** не хранятся, здесь нельзя посмотреть фильм или послушать музыку.  

В каждой категории есть **произведения**: книги, фильмы или музыка.  

Произведению может быть присвоен **жанр (Genre)** из списка предустановленных. Новые жанры может создавать только администратор.  

Благодарные или возмущённые пользователи оставляют к произведениям текстовые **отзывы (Review)** и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — **рейтинг** (целое число). На одно произведение пользователь может оставить только один отзыв.  

# Технологии

- [Python 3.8.8](https://www.python.org/downloads/release/python-388/)
- [Django 2.2.16](https://www.djangoproject.com/download/)
- [Django Rest Framework 3.12.4](https://www.django-rest-framework.org/)
- [PostgreSQL 13.0](https://www.postgresql.org/download/)
- [gunicorn 20.0.4](https://pypi.org/project/gunicorn/)
- [nginx 1.21.3](https://nginx.org/ru/download.html)

# Контейнер
- [Docker 20.10.14](https://www.docker.com/)
- [Docker Compose 2.4.1](https://docs.docker.com/compose/)

# URL's
- http://84.252.143.225/api/v1
- http://84.252.143.225/admin
- http://84.252.143.225/redoc

# Установка

Клонируйте репозиторий:
```sh
git clone https://github.com/ArtTRTR/yamdb_final.git
```
Перейдите в директорию с файлом _docker-compose.yaml_ и запустите контейнеры:
```sh
cd infra && docker-compose up -d --build
```
После успешного запуска контейнеров выполните миграции в проекте:
```sh
docker compose exec web python manage.py makemigrations
```
```sh
docker compose exec web python manage.py migrate
```
Создайте суперпользователя:
```sh
docker compose exec web python manage.py createsuperuser
```
Соберите статику:
```sh
docker compose exec web python manage.py collectstatic --no-input
```
Создайте дамп (резервную копию) базы данных:
```sh
docker compose exec web python manage.py dumpdata > fixtures.json
```
Для остановки контейнеров и удаления всех зависимостей воспользуйтесь командой:
```sh
docker compose down -v
```

# Документация

Для просмотра документации к API перейдите по адресу:
http://84.252.143.225/redoc/

# Примеры запросов

**GET**: http://84.252.143.225/api/v1/categories/

**POST**: http://84.252.143.225/api/v1/categories/ 
#### Тело запроса:
```json
{
  "name": "string",
  "slug": "string"
}
```
**GET**: http://84.252.143.225/api/v1/users/

## License

MIT

**Free Software**
