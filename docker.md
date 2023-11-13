docker
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




