alembic
=======

Alembic is a very useful library we can use for our database migrations. when we are working with Flask Framework we need a tool which can handle the database migrations. Alembic is widely used for migrations. Let us start how to use to alembic.

First, install the alembic in your virtual environment

```py
pip install alembic
```

After installing the alembic we need to initialize the alembic to our working project directory.
```py
alembic init alembic
```
After using this command you will see some files and folders are created in your project directory.

```
<project root>
├── src
│   └── <top-level package dir>
│       ├── alembic
│       │   ├── env.py
│       │   ├── README
│       │   ├── script.py.mako
│       │   └── versions
│       │       ├── 58c8dcd5fbdc_revision_1.py
│       │       └── ec385b47da23_revision_2.py
│       ├── alembic.ini
│       ├── __init__.py
│       └── <other files and dirs>
└── <other files and dirs>
```
As shown above such find of folder structure you will see after the init command. Currently, there will be no version files in your versions directory because we haven’t made any migrations yet. Now to use alembic we need to do certain changes in these files. First, change the sqlalchemy.url in your alembic.ini file.
```py
sqlalchemy.url = mysql+mysqldb://root:root@localhost:3306/database_name
```
Now we need to give our database models to alembic. Let’s take the sample model example.
```py
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, TIMESTAMP, text, JSON
from sqlalchemy.dialects.mysql import INTEGER

Base = declarative_base()
metadata = Base.metadata
class Student(Base):

    __tablename__ = 'student'

    id = Column(INTEGER(11), primary_key=True)
    enroll = Column(INTEGER(11))
    personal_info = Column(JSON)
    name= Column(String(255))
    created_on = Column(TIMESTAMP, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
```
As shown above, it is our model.py file.

Now in env.py in our alembic folder, we have to make some changes. To detect auto changes by alembic we need to give our model path to env.py
```py
from model import Base
target_metadata = [Base.metadata]
```
As shown above, we have to give the model base file to alembic env file. Now we are all set for our first migration.
```
alembic revision — autogenerate -m “First commit”
```
Using the above command alembic generate our first migration commit file in versions folder. you can see the version file now in the versions folder.

Once this file generates we are ready for database migration.
```py
alembic upgrade head
```
Once you run the above command your tables will be generated in your database.