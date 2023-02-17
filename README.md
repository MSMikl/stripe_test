# Тестовое задание

## Сайт на Django с оплатой через stripe

## Доступная тестовая страница

https://tg.michalbl4.ru/item/1

Развернута на своем собственном домашнем сервере в Docker. База данных - PostgreSQL в отдельном контейнере. Поменял бы доменное имя, но у Selectel какие-то проблемы с панелью управления DNS-хостингом, создать новую CNAME-запись нельзя, пришлось брать из уже имеющихся

## Предварительная подготовка

Для использования сайта необходимо зарегистрироваться на https://stripe.com и получить секретный и публичный ключи https://stripe.com/login?redirect=/account/apikeys


## Установка в режиме разработчика

Для работы необходим Python версии 3.11

Скачайте содержимеое репозитория себе на ПК. Установите зависимости командой

``` pip install -r requirements.txt ```

Создайте файл `.env`, в котором укажите следующие переменные

```
STRIPE_SECRET_KEY = {секретный ключ  Stripe}
STRIPE_PUBLIC_KEY = {публичный ключ Stripe}
```

Запустите миграции командой 

````
python3 manage.py migrate
````

Создайте суперпользователя командой

```
python3 manage.py createsuperuser
````

Запустите сервер в режиме разработки:

```
python3 manage.py runserver
```

Зайдите в административную панель сайта по адресу https://127.0.0.1:8000/admin и создайте товар (можно в перспективе добавить в админке кнопку прямого перехода к товару на сайте).

Перейдите по адресу https://127.0.0.1/item/1/

По нажатию на кнопку "Купить" происходит переход на страницу оплаты.

## Развертывание в продакшен

Развернуть сайт в продакшен можно в docker-контейнере. Помимо самого контейнера с django устанавливается обратный прокси nginx для раздачи статических файлов.

Для этого следует отредактировать файл `docker-compose.yml`, вписав в него указанные там перменные.

Данные для подключения к внешней базе данных, например, PostgreSQL, следует указывать в параметре `DB_URL` по следующей инструкции: https://github.com/jazzband/dj-database-url#url-schema

Если сайт разворачивается на домене, отличном от http://127.0.0.1, обязательно следует указать адрес в параметре `SITE_URL`.

После этого запустите сборку и запуск контейнеров командой

```
docker-compose up --build
```

Откройте новый терминал и примените миграции командой

```
docker-compose run --rm testshop bash -c "python3 manage.py migrate"
```

Создайте суперпользователя командой

```
docker-compose run --rm testshop bash -c "python3 manage.py superuser"
```

В административной панели по адресу {SITE_URL}/admin создайте товар, после чего перейдте по адресу {SITE_URL}/item/1 и нажмите "Купить"

### Примечание:

Web-дизайн - не моя сильная сторона. Для странички товара нашел какой-то произвольный шаблон, с шаблоном страницы результата вообще не заморачивался.
