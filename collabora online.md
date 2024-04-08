collabora online
================
Бесплатно только CODE версия, для теста это неважно, но если интегрировать на сайте это не рекомендуют (причин не приводят особо, кроме меньше числа пользователей, правда не ясно, всего пользователей в системе, или пользователей одновременно онлайн).
[Subscriptions - Collabora Office and Collabora Online](https://www.collaboraoffice.com/subscriptions/)

---
[collabora-online-sdk-examples/webapp/python at master · CollaboraOnline/collabora-online-sdk-examples · GitHub](https://github.com/CollaboraOnline/collabora-online-sdk-examples/tree/master/webapp/python)

[GitHub - CollaboraOnline/collabora-online-nuxeo-addon](https://github.com/CollaboraOnline/collabora-online-nuxeo-addon)


[Installation Guide — SDK https://sdk.collaboraonline.com/ documentation](https://sdk.collaboraonline.com/docs/installation/index.html)

[Docker image hub for CODE](https://hub.docker.com/r/collabora/code/)

[WOPI REST API Reference | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/)

Наиболее важная инфо для интерграции в стороние приложения, [How to integrate — SDK https://sdk.collaboraonline.com/ documentation](https://sdk.collaboraonline.com/docs/How_to_integrate.html)



---

Демо  [Your Collabora Online Demo](https://demo.eu.collaboraonline.com/owncloud/index.php/login)

Username: kireev20000@mail.ru, Password: owncloud1234



wopi protocol python

---

### WOPI Протокол
  WOPI, or Web Application Open Platform Interface, refers to a sequence of operations that allows users to gain access to a server and change files and data stored within it.

As a REST-based protocol, in order for the process to work HTTP requests need to be sent to a set of defined operations and REST endpoints. Therefore, in order to embed web-based Office document editing in your web Application, WOPI must be developed as a RESTful web API for implementation. You don’t need to implement the whole protocol; you only need to implement the methods of the protocol that are required for your web Application.

- It’s easier because it’s just a simple API implementation.
- It’s harder because the documentation for that implementation is very poor and lacks a complete working example.


WOPI on the other hand is the recommended backend storage. WOPI is Web Application Open Platform Interface, a protocol based on open standard for remote document access with authentication. Collabora Online accepts connection requests only from trusted WOPI hosts. The administrator has to list the host names and/or IP addresses of these trusted WOPI hosts in the storage.wopi block. Please note that connection requests from the same machine are always accepted.

---
Грубый набросок плана

1) Ставим в докер или нативно?
2) настроить WOPI хост
3) Проверить эндпоинты , и в целом разобраться как работает методом научного тыка на простом примере
4) Искать способы как это интегрировать в ЭПР