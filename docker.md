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

