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
---
## Routing in FastAPI

---
### Routing with the APIRouter class

The APIRouter class works in the same way as the FastAPI class does. However, uvicorn cannot use the APIRouter instance to serve the application, unlike the FastAPIs. Routes defined using the APIRouter class are added to the fastapi instance to enable their visibility. To enable the visibility of the routes, we’ll include the router path operations handler to the primary FastAPI instance using the include_router() method.

```py
from fastapi import FastAPI, APIRouter
from todo import todo_router

app = FastAPI()

@app.get("/hello")
async def say_hello() -> dict:
    return {'message': 'Hello!'}

app.include_router(todo_router)

---
todo.py

from fastapi import APIRouter

todo_router = APIRouter()

@todo_router.get("/todo")
async def todo_list_get() -> dict:
    return {
        "Список дел": todo_list
    }
```
---
### Validating Pydantic models and Nested models

Nested models - Pydantic models can also be nested, such as the following:
```py

class Item(BaseModel)
item: str
status: str

class Todo(BaseModel)
id: int
item: Item

As a result, a todo of type Todo will be represented as the following:
{
    "id": 1,
    "item": {
             "item": "Nested models",
             "Status": "completed"
            }
}
```
### Path and query parameters

FastAPI also provides a Path class that distinguishes path parameters from other arguments present in the route function. The Path class also helps give route parameters more context during the documentation automatically provided by OpenAPI via Swagger and ReDoc and acts as a validator.
```py
@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
```
Path(..., kwargs). The Path class takes a first positional argument set to None or ellipsis (...). If the first argument is set to an ellipsis (...), the path parameter becomes required. The Path class also contains arguments used for numerical  validations if a path parameter is a number. Definitions include gt and le – gt means greater than and le means less than. When used, the route will validate the path parameter against these arguments.

---
### Query parameters

A query parameter is an optional parameter that usually appears after a question mark in a URL. 
In a route handler function, an argument that isn’t homonymous with the path parameter is a query. You can also define a query by creating an instance of the FastAPI Query() class in the function argument, such as the following:
```py
async query_route(query: str = Query(None):
    return query
```
The POST method is used when an insertion into the server is to be made, and the UPDATE method is used when existing data in the server is to be updated.

---
## FastAPI Automatic Docs
Swagger - http://127.0.0.1:8000/docs
ReDoc - http://127.0.0.1:8000/redoc

```py
class Todo(BaseModel):
    id: int
    item: str

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "item": "Example Schema!"
            }
        }
```
---

## Response Models and Error Handling


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```


```py

```



























