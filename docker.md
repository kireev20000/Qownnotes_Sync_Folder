# Docker

docker run -t -d -p 9980:9980 -e "extra_params=--o:ssl.enable=false" collabora/code:22.05.10.2.1


копирование файлов из контейнера.
```
docker cp <containerId>:/file/path/within/container /host/path/target
docker cp d537be3137f859effa67dde813d34a5a12a6e6c6190510f6c322bca6bcf5972f://etc/coolwsd/coolwsd.xml b:/coolwsd.xml
```
пропись путей для винды 0
```
    volumes:
      - "B:/_WorkLab/_other/colla_lab_example/flask_collabora/pyscripts:/opt/collaboraoffice/share/Scripts/python"
```
выполни команду sudo docker exec -it -u=root имя контейнера /bin/bash (в винде без судо)
sudo apt install inetutils-ping - установка пинга в контейнер 
apt install mc - midnight commander

собрать файл
```
docker build -t image_name .
```
## Подготовка и запуск проекта production
### Склонировать репозиторий:
```
git clone 
```
- Соберите докер-образ из рабочей директории:***
```shell
docker build -t flask_test_case .
```

- Cоздать и заполнить .env файл в директории infra
```
FLASK_APP=app
FLASK_DEBUG=False
SECRET_KEY_JWT='ваш секретный ключ'
DATABASE_URL ='postgresql://postgres:postgres@db:5432/maindb'
COMPOSE_PROJECT_NAME="test_case_rg"
```

- Запускаем docker-compose из директории infra:
```shell
docker compose -f docker-compose.production.yml up
```

Имя хоста в PGAdmine db, а не локалхост и т.д.

docker compose -f docker-compose.production.yml up 



## Что такое контейнеризация? Зачем она нужна?
Контейнеризация — это технология, которая помогает запускать приложения изолированно от основной операционной системы. Программа упаковывается в специальную оболочку-контейнер, внутри которой — среда, необходимая для работы.

Технология нужна для:

1. для изолированного запуска приложений и рабочих сред вне зависимости от системы и ПО, установленных на конкретной машине;
2. контроля ресурсов и снижения нагрузки на систему;
3. разрешения конфликтов, которые могут возникнуть из-за того, что разные приложения нуждаются в различных версиях ПО или библиотек;
4. быстрого перемещения настроенных приложений и сред с одной машины на другую;
5. создания удобной рабочей инфраструктуры;
6. ускорения процесса разработки и снижения риска ошибок;
7. масштабирования готовых решений;
8. легкого управления сложными приложениями, средами и системами. 

## Чем контейнер отличается от виртуальной машины?
Основное различие контейнеров и виртуальных машин заключается в том, что виртуальные машины виртуализируют весь компьютер вплоть до аппаратных уровней, а контейнеры — только программные уровни выше уровня операционной системы.

## Что такое образ?
Image. Неизменяемый файл (образ), из которого можно неограниченное количество раз развернуть контейнер.

Образ Docker (Docker Image) - это неизменяемый файл, содержащий исходный код, библиотеки, зависимости, инструменты и другие файлы, необходимые для запуска приложения.

Из-за того, что образы предназначены только для чтения их иногда называют снимками (snapshot).Они представляют приложение и его виртуальную среду в определенный момент времени. Такая согласованность является одной из отличительных особенностей Docker. Он позволяет разработчикам тестировать и экспериментировать программное обеспечение в стабильных, однородных условиях.

## Что такое том?
Том Docker — это средство для постоянного хранения информации на виртуальной машине. Данные в томе хранятся независимо от контейнеров. Если вы удалите контейнер, тома и данные в томах останутся. Удаление тома — отдельная операция.

Тома для постоянного хранения информации. По умолчанию в Docker папки хранилищ создаются на хост-машине, но предусмотрена и возможность подключения удаленных хранилищ

## Что такое сеть контейнера?
Сеть Docker в основном используется для установления связи между контейнерами Docker и внешним миром через хост-машину, или вы можете сказать, что это коммуникационный канал, через который все изолированные контейнеры взаимодействуют друг с другом в различных ситуациях для выполнения необходимых действий.

## Какие виды сетей бывают?

1. Bridge network при запуске Docker автоматически создается сеть типа мост по умолчанию. Недавно запущенные контейнеры будут автоматически подключаться к нему. Вы также можете создавать пользовательские настраиваемые мостовые сети. Пользовательские мостовые сети превосходят сетевые мосты по умолчанию.
2. Host network : удаляет сетевую изоляцию между контейнером и хостом Docker и напрямую использует сеть хоста. Если вы запускаете контейнер, который привязывается к порту 80, и вы используете хост-сеть, приложение контейнера доступно через порт 80 по IP-адресу хоста. Означает, что вы не сможете запускать несколько веб-контейнеров на одном хосте, на одном и том же порту, так как порт теперь является общим для всех контейнеров в сети хоста.
3. None network : в сети такого типа контейнеры не подключены ни к одной сети и не имеют доступа к внешней сети или другим контейнерам. Итак, эта сеть используется, когда вы хотите полностью отключить сетевой стек в контейнере.
4. Overlay network : Создает внутреннюю частную сеть, которая охватывает все узлы, участвующие в кластере swarm. Таким образом, оверлейные сети облегчают обмен данными между сервисом Docker Swarm и автономным контейнером или между двумя автономными контейнерами на разных демонах Docker.
5. Macvlan network : Некоторые приложения, особенно устаревшие приложения, отслеживающие сетевой трафик, ожидают прямого подключения к физической сети. В такой ситуации вы можете использовать сетевой драйвер Macvlan для назначения MAC-адреса виртуальному сетевому интерфейсу каждого контейнера, что делает его физическим сетевым интерфейсом, напрямую подключенным к физической сети.

[🐳 Объяснение концепции сетей в Docker – IT is good](https://itisgood.ru/2019/10/29/objasnenie-koncepcii-setej-v-docker/)

---
## Зачем нужен docker-compose?
В составе Docker есть инструмент, который позволяет централизованно запускать большое количество сервисов: Docker Compose. Документирование и конфигурирование сервисов приложения осуществляется с помощью текстового YAML-файла. Команда docker‑compose up развертывает сервисы приложений и создает из образа новые контейнеры, а также сети, тома и все конфигурации, указанные в файле Docker Compose.

На этапе тестирования разработчикам приходится создавать изолированные среды, а потом уничтожать их. Docker Compose позволяет создать и уничтожить среду путем ввода нескольких команд. К участию в проекте можно привлекать и сторонних пользователей.

## Оркестрация
Когда контейнеров становится слишком много, ими трудно управлять. На помощь приходят системы оркестрации.

### Docker Swarm
Стандартная система оркестрации контейнеров, достаточная для решения базовых задач. Позволяет быстро создать из нескольких хостов с контейнерами последовательный кластер Swarm, считая все кластерные хосты единым контейнерным пространством. В Docker-кластере должна быть как минимум одна управляющая нода (manager).

### Kubernetes
Платформа для автоматизации работы с контейнерами на Ubuntu, CentOS и других ОС Linux. Позволяет централизованно группировать контейнеры, балансировать нагрузку, активировать сервисы из сотен приложений одновременно. Kubernetes предоставляет пользователям больше возможностей по сравнению со Swarm, но и настраивать его сложнее.»

- RabbitMQ - [Хабр](https://habr.com/ru/post/149694/)
- Docker - [Хабр](https://habr.com/ru/company/ruvds/blog/438796/)




========================
dockerfile
```yaml
FROM python:3.10

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

```

docker build --tag python-django .
docker run --publish 8000:8000 python-django


----

docker run -it --rm --name redis -p 6379:6379 redis
Эта команда запускает Redis в контейнере Docker. Опция -it сообщает Docker, что можно переходить прямо внутрь контейнера для интерактивного ввода. Параметр --rm сообщает Docker, что при выходе из контейнера нужно очищать контейнер и удалять файловую систему автоматически. Опция --name используется для назначения контейнеру имени. Опция -p применяется для публикации порта 6379, на котором работает Redis, на тот же порт интерфейса хоста. В Redis по умолчанию используется порт 6379.

---
## Деплой Диплома 
cd frontend  # В директории frontend...
docker build -t kireev20000/kittygram_frontend .

cd ../backend  # То же в директории backend…
docker build -t kireev20000/kittygram_backend .

cd ../gateway  # ...то же и в gateway.
docker build -t kireev20000/kittygram_gateway .

docker push kireev20000/kittygram_frontend
docker push kireev20000/kittygram_backend
docker push kireev20000/kittygram_gateway

docker compose -f docker-compose.production.yml up

docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.production.yml exec backend cp -r /app/static_backend/. /backend_static/static/

sudo systemctl stop gunicorn-kittygram.service
sudo rm /etc/systemd/system/gunicorn-kittygram.service

scp -i yc-kireev20000 docker-compose.production.yml yc-user@158.160.68.229:/home/yc-user/kittygram/docker-compose.production.yml
scp -i yc-kireev20000 .env yc-user@158.160.68.229:/home/yc-user/kittygram/.env

sudo docker compose -f docker-compose.production.yml exec backend python manage.py migrate
sudo docker compose -f docker-compose.production.yml exec backend python manage.py collectstatic
sudo docker compose -f docker-compose.production.yml exec backend cp -r /app/static_backend/. /backend_static/static/

sudo nano /etc/nginx/sites-enabled/default
sudo nginx -t
sudo service nginx reload

sudo journalctl --vacuum-size=1M
docker system prune
df -h

npm cache clean
sudo apt-get clean
docker system prune -a 
journalctl --vacuum-size=100M 
journalctl --vacuum-time=1d 
journalctl --vacuum-files=10

npm cache clean не сработает без ключа --force


А кто как на сервер закидывал docker-compose.yml и nginx файлы, я вот вручную скопировал, не могу найти команду как это сделать через workflow, вроде делали как то?
uses: appleboy/scp-action@master
        with:
          host: ${{ secrets.HOST }}
          username: ${{ secrets.USER }}
          key: ${{ secrets.SSH_KEY }}
          passphrase: ${{ secrets.SSH_PASSPHRASE }}
          source: "infra/docker-compose.production.yml,infra/nginx.conf"
          target: "foodgram/"
          strip_components: 1
          
          
docker compose -f имя_файла_композа up




