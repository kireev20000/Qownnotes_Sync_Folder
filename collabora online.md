collabora online
================
Бесплатно только CODE версия, для теста это неважно, но если интегрировать на сайте это не рекомендуют (причин не приводят особо, кроме меньшего числа пользователей, правда не ясно, всего пользователей в системе, или пользователей одновременно онлайн).
[Subscriptions - Collabora Office and Collabora Online](https://www.collaboraoffice.com/subscriptions/)

``Здесь разворачивание на своих серверах доступно бесплатно, но готовые пакеты имеют ограничение по количеству активных пользователей — это решается самостоятельной сборкой из исходников, благо проект с открытым исходным кодом. ``

---
Демо  [Your Collabora Online Demo](https://demo.eu.collaboraonline.com/owncloud/index.php/login)
Username: kireev20000@mail.ru, Password: owncloud1234

---
Пример интеграции в Джанго 3.1, очень базово -  [collabora-online-sdk-examples/webapp/python at master · CollaboraOnline/collabora-online-sdk-examples · GitHub](https://github.com/CollaboraOnline/collabora-online-sdk-examples/tree/master/webapp/python)

Аддоны на питоне сомнительной полезности -[GitHub - CollaboraOnline/collabora-online-nuxeo-addon](https://github.com/CollaboraOnline/collabora-online-nuxeo-addon)


Гайд по установки хоста, либо нативно, либо в докер[Installation Guide — SDK https://sdk.collaboraonline.com/ documentation](https://sdk.collaboraonline.com/docs/installation/index.html)

Докер образ Collabora Online Development ED - [Docker image hub for CODE](https://hub.docker.com/r/collabora/code/)

---

### Интерграция

Наиболее важная инфо для интерграции в стороние приложения, [How to integrate — SDK https://sdk.collaboraonline.com/ documentation](https://sdk.collaboraonline.com/docs/How_to_integrate.html)

---
### WOPI Протокол

WOPI REST API Reference - базавое описание протокола WOIP
 [WOPI REST API Reference | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/)

In addition to the basics of WOPI as described in WOPI specifications, Collabora Online implements various extensions, in addition to those outlined above primarily associated with CheckFileInfo, to support some features that you may find useful.


  WOPI, or Web Application Open Platform Interface, refers to a sequence of operations that allows users to gain access to a server and change files and data stored within it.

As a REST-based protocol, in order for the process to work HTTP requests need to be sent to a set of defined operations and REST endpoints. Therefore, in order to embed web-based Office document editing in your web Application, WOPI must be developed as a RESTful web API for implementation. You don’t need to implement the whole protocol; you only need to implement the methods of the protocol that are required for your web Application.

- It’s easier because it’s just a simple API implementation.
- It’s harder because the documentation for that implementation is very poor and lacks a complete working example.


WOPI on the other hand is the recommended backend storage. WOPI is Web Application Open Platform Interface, a protocol based on open standard for remote document access with authentication. Collabora Online accepts connection requests only from trusted WOPI hosts. The administrator has to list the host names and/or IP addresses of these trusted WOPI hosts in the storage.wopi block. Please note that connection requests from the same machine are always accepted.

---
Грубый набросок плана

1) Ставим в докер или нативно?
2) настроить WOPI хост.
3) Проверить эндпоинты , и в целом разобраться как работает методом научного тыка на простом примере
4) Искать способы как это интегрировать в ЭПР.

[Офф план интеграции по примерным шагам - Step-by-step tutorial — SDK https://sdk.collaboraonline.com/ documentation](https://sdk.collaboraonline.com/docs/Step_by_step_tutorial.html)

может и не надо будет, настройка сервера коде - [Install and Configure Collabora CODE](https://www.linode.com/docs/guides/how-to-install-collabora-code/)

---
### Видео с конференций о интеграции

видео о интеграции с конференции, примерно тоже самое что в доках, скорее просто обзор возможностей -  [Easy to set up – Anywhere. Integrating Collabora Online Into Your Services 🆒 COOL Days 2021 - YouTube](https://www.youtube.com/watch?v=K8Dw7CWZkVc)

[Setting up your own Collabora Online - COOL Days 2021 - YouTube](https://www.youtube.com/watch?v=m-N_wnV-eJw)

[SDK: creating a new integration - COOL Days 2021 - YouTube](https://www.youtube.com/watch?v=Gy6MFHYugN4&list=PLeh8MeOzF8jals5oAfZlYmksVaLfY6Wxv&index=3)

[Bringing Collabora Online to your web app Its easy to add rich document collaboration to your web a… - YouTube](https://www.youtube.com/watch?v=H7HfbZBycRU)
[Файл презентации с этого видео, нашел в другом месте](https://archive.fosdem.org/2020/schedule/event/bringing_collabora_online_webapp/attachments/slides/4143/export/events/attachments/bringing_collabora_online_webapp/slides/4143/collaborative.pdf)

[Integrate Collabora Online with web applications - YouTube](https://www.youtube.com/watch?v=xaN10p5inx8)


