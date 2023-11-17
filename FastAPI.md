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
---
## Jinja2 templates in FastAPI

The Jinja templating engine makes use of curly brackets { } to distinguish its expressions and syntax from regular HTML, text and any other variable in the template file. The {{ }} syntax is called a variable block. The {% %} syntax houses control structures such as if/else, loops, and macros.
The three common syntax blocks used in the Jinja templating language include the following:
1) {% … %} – This syntax is used for statements such as control structures.
2) {{ todo.item }} – This syntax is used to print out the values of the expressions passed to it.
3) {# This is a great API book! #} – This syntax is used when writing comments and is not displayed on the web page.

Jinja template variables can be of any Python type or object if they can be converted into strings. A model, list, or dictionary type can be passed to the template.

### Filters

Despite the similarity between Python and Jinja’s syntax, modifications such as joining strings, setting the first character of a string to uppercase, and so on cannot be done using Python’s syntax in Jinja. Therefore, to perform such  modifications, we have filters in Jinja. A filter is separated from the variable by a pipe symbol (|) and may entertain optional arguments in parentheses. A filter is defined in this format:

```py
    {{ variable | filter_name(*args) }}

If there are no arguments, the definition becomes the following:

    {{ variable | filter_name }}
    
The default filter variable is used to replace the output of the passed value if it turns out to be None:

{{ todo.item | default('This is a default todo item') }}
This is a default todo item

The escape filter. This filter is used to render raw HTML output:
{{ "<title>Todo Application</title>" | escape }}
<title>Todo Application</title>

Using if statements. The usage of if statements in Jinja is similar to their usage in Python. if statements are used in the {% %} control blocks. Let’s look at an example:

{% if todo | length < 5 %}
    You don't have much items on your todo list!
{% else %}
    You have a busy day it seems!
{% endif %}

Loops. We can also iterate through variables in Jinja. This could be a list or a general function, such as the following, for example:
{% for todo in todos %}
    <b> {{ todo.item }} </b>
{% endfor %}

You can access special variables inside a for loop, such as loop.index, which gives
the index of the current iteration. 
```
[Template Designer Documentation — Jinja Documentation (3.0.x)](https://jinja.palletsprojects.com/en/3.0.x/templates/#builtin-filters) 


---
### Macros in Jinja
A macro in Jinja is a function that return an HTML string. The main use case for macros is to avoid the repetition of code and instead use a single function call. For example, an input macro is defined to reduce the continuous definition of input tags in an HTML form:

```html
    {% macro input(name, value='', type='text', size=20 %}
      <div class="form">
      <input type="{{ type }}" name="{{ name }}" value="{{ value|escape }}"               size="{{ size }}">
      </div>
    {% endmacro %}

Now, to quickly create an input in your form, the macro is called:

    {{ input('item') }}

This will return the following:

    <div class="form">
      <input type="text" name="item" value="" size="20">
    </div>
```
## Authentication methods in FastAPI

FastAPI supports the common authentication methods of basic HTTP authentication, cookies, and bearer
token authentication. Let’s briefly look at what each method entails: 

1) Basic HTTP authentication: In this authentication method, the user credentials, which is usually a username and password, are sent via an Authorization HTTP header. The request in turn returns a WWW-Authenticate header containing a Basic value and an optional realm parameter, which indicates the resource the authentication request is made to.
2) Cookies: Cookies are employed when data is to be stored on the client side, such as in web browsers. FastAPI applications can also employ cookies to store user data, which can be retrieved by the server for authentication purposes. 
3) Bearer token authentication: This method of authentication involves the use of  security tokens called bearer tokens. These tokens are sent alongside the Bearer keyword in an Authorization header request. The most used token is JWT, which is usually a dictionary comprising the user ID and the token’s expiry time

## Dependency injection

Dependency injection is a pattern where an object – in this case, a function – receives an instance variable needed for the further execution of the function.

[Внедрение зависимостей проще простого – на Python / Хабр](https://habr.com/ru/companies/piter/articles/648299/)
[Understanding Dependencies / Хабр](https://habr.com/ru/articles/349836/)
[Dependency injection в Python простыми словами / Dependency Injector - YouTube](https://www.youtube.com/watch?v=mJI7MzRCVkQ)

In FastAPI, dependencies are injected by declaring them in the path operation function arguments.
In FastAPI, a dependency can be defined as either a function or a class. The dependency created gives us access to its underlying values or methods, eliminating the need to create these objects in the functions inheriting them. Dependency injection helps in reducing code repetition in some cases, such as in enforcing authentication and authorization.

```py
from fastapi import Depends

@router.get("/user/me")
async get_user_details(user: User = Depends(get_user)):
    return user
```
The route function here is dependent on the get_user function, which serves as its dependency. What this means is that to access the preceding route, the get_user dependency must be satisfied. 
The Depends class, which is imported from the FastAPI library, is responsible for taking the function passed as the argument and executing it when the endpoint is called, automatically making available to the endpoint, they return value of the function passed to it.

---
Depends импортируется с fastapi
from fastapi import Depends

и ее пишут для удобства. Типо чтобы не прописывать аргументы вручную, а указать уже на существующие требования для какой то функции. Типо так

def func1(arg1, arg2):
    return arg1, arg2

def func2(Depends(func1)):
return arg1, arg2

Вот во вторую функцию типо мы не прописывали arg1, arg2, но они ожидаются там

[Dependencies - FastAPI](https://fastapi.tiangolo.com/tutorial/dependencies/#__tabbed_1_1)
```py

```
## What is a middleware?
A middleware is a function that acts as an intermediary between an operation. In web APIs, a middleware serves as an mediator in a request-response operation.


## Configuring CORS

Cross-Origin Resource Sharing (CORS) serves as a rule that prevents unregistered clients access to a resource.
FastAPI provides a CORS middleware, CORSMiddleware, that allows us to register domains which can access our API. The middleware takes an array of origins which will be permitted to access the resources on the server

```py
from fastapi.middleware.cors import CORSMiddleware

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```
## Testing FastAPI Applications
154  страница Building Python Web APIs with FastAPI A fast paced guide to building (2022) Adeshina

Unit testing is a testing procedure where individual components of an application are tested. This form of testing enables us to verify the working capability of individual components. For example, unit tests are employed in testing individual routes in an application to ensure the proper responses are returned.

The standard practice is to define the functions that will be tested in an external location. This file is then imported and the functions to be tested are invoked in the test functions.

Fixtures are reusable functions defined to return the data needed in test functions. Fixtures are decorated with the pytest.fixture decorator.
```py
import pytest

from models.events import EventUpdate

# Fixture is defined.
@pytest.fixture
def event() -> EventUdpate:
    return EventUpdate(
        title="FastAPI Book Launch",
        image="https://packt.com/fastapi.png",
        description="We will be discussing the contents of the FastAPI book in this event.Ensure to come with your own copy to win gifts!",
        tags=["python", "fastapi", "book", "launch"],
        location="Google Meet"
)

def test_event_name(event: EventUpdate) -> None:
    assert event.title == "FastAPI Book Launch"
    
```
## Подключение к БД синтаксис:



```py
DATABASE_URL = "postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
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



























