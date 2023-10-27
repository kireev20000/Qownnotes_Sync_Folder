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

### What is a response header?
A response header consists of the request's status and additional information to guide the delivery of the response body. An example of the information contained in the response header is Content-Type, which tells the client the content type returned. 

### What is a response body?
The response body, on the other hand, is the data requested from the server by the client. The response body is determined from the Content-Type header variable and the most commonly used one is application/json.

### Status codes
Status codes are unique short codes issued by a server in response to a client’s request. Response status codes are grouped into five categories, each denoting a different response:

- 1XX: Request has been received.
- 2XX: The request was successful.
- 3XX: Request redirected.
- 4XX: There’s an error from the client.
- 5XX: There’s an error from the server.Building response models 45

A complete list of HTTP status codes can be found at https://httpstatuses.com/

---
### Building response models



```py
--- model.py
class Todo(BaseModel):
    id: int
    item: str
    
class TodoItem(BaseModel):
    item: str

class TodoItems(BaseModel):
    todos: List[TodoItem]

--- app.py

@todo_router.get("/todo", response_model=TodoItems)
async def retrieve_todo() -> dict:
    return {
        "todos": todo_list
    }
--- результат
в ответе отображается только item, без id
    
```
---

### Error handling
Errors in FastAPI are handled by raising an exception using FastAPI’s HTTPException class. The HTTPException class takes three arguments:

• status_code: The status code to be returned for this disruption
• detail: Accompanying message to be sent to the client
• headers: An optional parameter for responses requiring headers

```py
from fastapi import APIRouter, Path, HTTPException, status

@todo_router.get("/todo/{todo_id}")
async def get_single_todo(todo_id: int = Path(..., title="The ID of the todo to retrieve.")) -> dict:
    for todo in todo_list:
        if todo.id == todo_id:
            return {
                "todo": todo
            }
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo with supplied ID doesn't exist",
    )
```
We can declare the HTTP status code to override the default status code for successful operations by adding the status_code argument to the decorator function:

```py
@todo_router.post("/todo", status_code=201)
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {
        "message": "Todo added successfully."
    }
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



























