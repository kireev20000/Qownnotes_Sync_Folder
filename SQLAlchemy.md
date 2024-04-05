SQLAlchemy
==========
### What is the difference between the sqlalchemy load methods: joinedload, lazyload, defaultload and subqueryload?


    lazyload does not load immediately but waits for first access
    subqueryload and joinedload both load immediately the related collection, but by emitting different SQL. Even if the result is the same for both mode, there might be a large performance difference.

Assume a class A that hold a list of children towards both B and C:

class A:
    b_list = relationship(B, lazy='joined')
    c_list = relationship(C, lazy='joined')

class B:
    a_id = Column(ForeignKey('a.id'))

class C:
    a_id = Column(ForeignKey('a.id'))

If you set both b_list and c_list as joinedload, then the following sql will be emitted (or similar):

SELECT ... FROM A 
LEFT JOIN B ON B.a_id = A.id
LEFT JOIN C ON C.a_id = A.id
WHERE ...

If there is 1000 elements in both B and C, 1 000 000 rows will be returned, then sqlalchemy will sort out duplicates in python space. With large numbers and more relationships, it may even make your database or your application run out of memory.

subqueryload shouldn't have this problem, since all relations are loaded separately via a subquery. I'm not totally sure of the difference between subqueryload and selectinload, but according to the documentation, subqueryload is a legacy loader, and is superseded by selectinload.

For what it's worth, in our project, we use the following policy (that is actually automated):

    load single element relationships with joinedload.
    load collections with selectinload.

As for the difference between subqueryload and selectinload, the first emits sub-selects (SELECT ... FROM (SELECT ... lhs JOIN rhs ON ... WHERE ...) AS anon_1 JOIN rhs ON ...), while the latter generates two separate queries, first to query list of lhs` and then generates a second query for rhs with WHERE rhs.lhs_id IN (...) for all the lhs.id that got matched.

---
