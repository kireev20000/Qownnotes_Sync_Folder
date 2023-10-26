FastAPI
=======

## Книги
Building Python Web APIs with FastAPI A fast paced guide to building (2022) Adeshina
Building Python Microservices with FastAPI Build secure, scalable (2022) Tragura

---
## Uvicorn

In the command, uvicorn takes the following arguments:
• file:instance: The file containing the instance of FastAPI and the name variable holding the FastAPI instance.
• --port PORT: The port the application will be served on.
• --reload: An optional argument included to restart the application on every file change.

``` py
pip install fastapi uvicorn

uvicorn api:app --port 8000 --reload
```

## Routing in FastAPI

