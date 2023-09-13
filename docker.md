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